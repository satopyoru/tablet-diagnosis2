import streamlit as st

# アプリの設定
st.set_page_config(
    page_title="子供のタブレット教材診断ツール",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# セッションステートの初期化
if 'page' not in st.session_state:
    st.session_state.page = 'home'

if 'question_stage' not in st.session_state:
    st.session_state.question_stage = 1

if 'answers' not in st.session_state:
    st.session_state.answers = {
        'grade': None,
        'subjects': [],
        'budget': 3000,
        'features': [],
        'purpose': None,
        'learning_style': None
    }

if 'recommendations' not in st.session_state:
    st.session_state.recommendations = []

# ナビゲーション関数（ボタンに紐づける関数）
def go_to_home():
    st.session_state.page = 'home'
    
def go_to_questionnaire():
    st.session_state.page = 'questionnaire'
    st.session_state.question_stage = 1

def go_to_results():
    if not st.session_state.recommendations:
        st.error("まずは診断を完了させてください")
    else:
        st.session_state.page = 'results'

def reset_session():
    st.session_state.page = 'home'
    st.session_state.question_stage = 1
    st.session_state.answers = {
        'grade': None,
        'subjects': [],
        'budget': 3000,
        'features': [],
        'purpose': None,
        'learning_style': None
    }
    st.session_state.recommendations = []

# ナビゲーション関数（質問間の移動）
def go_to_next_question():
    st.session_state.question_stage += 1

def go_to_prev_question():
    st.session_state.question_stage -= 1

# 質問内容を「スキップ」して診断結果を表示
def go_to_results_directly():
    # ここで簡易版の推薦アルゴリズムでレコメンデーションを作成
    from random import sample
    tablet_ids = ["challenge_touch", "smile_zemi", "z_kai_tablet", "risu_kids", "study_suppli"]
    st.session_state.recommendations = sample(tablet_ids, 3)
    st.session_state.page = 'results'

# モバイル表示のためのCSS設定
st.markdown("""
<style>
    /* タブを下部に配置するCSS */
    @media (max-width: 768px) {
        .stTabs [data-baseweb="tab-list"] {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            z-index: 999;
            padding: 10px 0;
            border-top: 1px solid #eee;
            display: flex;
            justify-content: space-around;
        }
        .main > div {
            padding-bottom: 60px;
        }
    }
    
    /* ボタンの見た目を改善 */
    .stButton button {
        width: 100%;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }
    
    /* プライマリボタンの色をより鮮やかに */
    .stButton button[kind="primary"] {
        background-color: #1E88E5;
    }
</style>
""", unsafe_allow_html=True)

# 基本的なデータ（最小限）
tablet_data = [
    {
        "id": "challenge_touch",
        "name": "チャレンジタッチ",
        "monthly_fee": 3250,  # 小1～2年生の場合（12ヶ月一括払い）
        "initial_fee": 0,
        "description": "ベネッセの「進研ゼミ」のタブレット版。基礎力養成を目的とした学習コンテンツと専用タブレットを提供。",
        "url": "https://jinzaikachi.com/challenge-campaign/"
    },
    {
        "id": "smile_zemi",
        "name": "スマイルゼミ",
        "monthly_fee": 3278,  # 小1～2年生の場合（12ヶ月一括払い）
        "initial_fee": 0,
        "description": "幼児から中学生まで対応した総合的なタブレット教材。AIが子どもの理解度に合わせて問題を出題。",
        "url": "https://jinzaikachi.com/smilezemi-campaign/"
    },
    {
        "id": "z_kai_tablet",
        "name": "Z会タブレットコース",
        "monthly_fee": 3570,  # 小1年生の場合（12ヶ月一括払い）
        "initial_fee": 0,
        "description": "思考力・表現力を重視した難関校受験にも対応する高品質な学習教材。",
        "url": "https://jinzaikachi.com/z-tablet/"
    },
    {
        "id": "risu_kids",
        "name": "RISU算数",
        "monthly_fee": 2948,  # 基本料金＋利用料が発生（進度に応じて変動）
        "initial_fee": 0,
        "description": "AIが子どもの理解度を精密に分析し、一人ひとりに最適な問題を提供する算数特化型教材。",
        "url": "https://jinzaikachi.com/risu-math/"
    },
    {
        "id": "study_suppli",
        "name": "スタディサプリ小学講座",
        "monthly_fee": 1815,  # 学年が上がっても定額
        "initial_fee": 0,
        "description": "有名講師による質の高い授業動画と演習問題を低価格で利用できるオンライン学習サービス。",
        "url": "https://jinzaikachi.com/study-supple/"
    }
]

# サイドバー（シンプル）
with st.sidebar:
    st.title("メニュー")
    
    # ボタンにコールバック関数を設定
    st.button("ホーム", key="sidebar_home", on_click=go_to_home)
    st.button("診断スタート", key="sidebar_start", on_click=go_to_questionnaire)
    st.button("結果を見る", key="sidebar_results", on_click=go_to_results)
    
    st.divider()
    st.button("リセット", key="sidebar_reset", on_click=reset_session)

# メインコンテンツ
if st.session_state.page == 'home':
    st.title("🎓 子供のタブレット教材診断ツール")
    
    st.markdown("""
    ### お子様に最適なタブレット教材を見つけましょう
    
    このツールでは、お子様の学年、興味のある科目、ご予算などに基づいて、
    最適なタブレット教材をご提案します。
    
    多くの選択肢があり、どれを選べばよいのか迷っている保護者の方々をサポートします。
    """)
    
    st.button("診断を始める", use_container_width=True, type="primary", key="home_start", on_click=go_to_questionnaire)
    
    st.button("すぐに結果を見る", key="home_skip", on_click=go_to_results_directly)

elif st.session_state.page == 'questionnaire':
    st.title("📝 お子様に最適な教材を見つけるための診断")
    
    # プログレスバーの表示
    progress = st.session_state.question_stage / 6
    st.progress(progress)
    st.write(f"ステップ {st.session_state.question_stage}/6")
    
    if st.session_state.question_stage == 1:
        st.header("Q1: お子様の学年を教えてください")
        
        grade_options = [
            "幼児（年少・年中・年長）",
            "小学校低学年（1〜3年生）",
            "小学校高学年（4〜6年生）"
        ]
        
        grade = st.radio(
            "学年を選択してください:",
            options=grade_options,
            index=None,
            key="grade_radio_q1"
        )
        
        grade_mapping = {
            "幼児（年少・年中・年長）": "kindergarten",
            "小学校低学年（1〜3年生）": "lower_elementary",
            "小学校高学年（4〜6年生）": "upper_elementary"
        }
        
        if grade:
            st.session_state.answers['grade'] = grade_mapping[grade]
        
        # 次へボタンを配置
        st.button("次へ", type="primary", key="next_q1", on_click=go_to_next_question, disabled=not grade)
    
    elif st.session_state.question_stage == 2:
        st.header("Q2: 学習したい科目を選択してください")
        
        subject_options = {
            "国語": "japanese",
            "算数/数学": "math",
            "英語": "english",
            "理科": "science",
            "社会": "social",
            "プログラミング": "programming",
            "思考力・論理的思考": "thinking",
            "アート・創造性": "art",
            "総合学習（複数科目）": "comprehensive"
        }
        
        selected_subjects = st.multiselect(
            "興味のある科目を選択してください（複数選択可）:",
            options=list(subject_options.keys()),
            default=[],
            key="subjects_multiselect_q2"
        )
        
        if selected_subjects:
            st.session_state.answers['subjects'] = [subject_options[subject] for subject in selected_subjects]
        
        # ボタン配置
        col1, col2 = st.columns(2)
        with col1:
            st.button("戻る", key="back_q2", on_click=go_to_prev_question)
        with col2:
            st.button("次へ", type="primary", key="next_q2", on_click=go_to_next_question, disabled=not selected_subjects)
    
    elif st.session_state.question_stage == 3:
        st.header("Q3: 学習の主な目的は何ですか？")
        
        purpose_options = [
            "学校の授業についていくため",
            "学習習慣を身につけるため",
            "中学受験の準備のため",
            "苦手科目を克服するため",
            "先取り学習・発展学習のため",
            "思考力・創造性を伸ばすため"
        ]
        
        purpose = st.radio(
            "最も当てはまるものを選んでください:",
            options=purpose_options,
            index=None,
            key="purpose_radio_q3"
        )
        
        purpose_mapping = {
            "学校の授業についていくため": "catch_up",
            "学習習慣を身につけるため": "habit_formation",
            "中学受験の準備のため": "exam_preparation",
            "苦手科目を克服するため": "weakness_improvement",
            "先取り学習・発展学習のため": "advanced_learning",
            "思考力・創造性を伸ばすため": "thinking_creativity"
        }
        
        if purpose:
            st.session_state.answers['purpose'] = purpose_mapping[purpose]
        
        # ボタン配置
        col1, col2 = st.columns(2)
        with col1:
            st.button("戻る", key="back_q3", on_click=go_to_prev_question)
        with col2:
            st.button("次へ", type="primary", key="next_q3", on_click=go_to_next_question, disabled=not purpose)
    
    elif st.session_state.question_stage == 4:
        st.header("Q4: お子様の好みの学習スタイルは？")
        
        style_options = [
            "動画授業で学ぶのが好き",
            "ゲーム感覚で楽しく学びたい",
            "自分のペースでコツコツ取り組みたい",
            "実験や体験を通して学びたい",
            "AIが個別対応してくれる学習がいい",
            "紙とデジタルの両方を使った学習がいい"
        ]
        
        style = st.radio(
            "最も当てはまるものを選んでください:",
            options=style_options,
            index=None,
            key="style_radio_q4"
        )
        
        style_mapping = {
            "動画授業で学ぶのが好き": "video_learning",
            "ゲーム感覚で楽しく学びたい": "gamified_learning",
            "自分のペースでコツコツ取り組みたい": "self_paced",
            "実験や体験を通して学びたい": "experiential_learning",
            "AIが個別対応してくれる学習がいい": "ai_adaptive",
            "紙とデジタルの両方を使った学習がいい": "hybrid_learning"
        }
        
        if style:
            st.session_state.answers['learning_style'] = style_mapping[style]
        
        # ボタン配置
        col1, col2 = st.columns(2)
        with col1:
            st.button("戻る", key="back_q4", on_click=go_to_prev_question)
        with col2:
            st.button("次へ", type="primary", key="next_q4", on_click=go_to_next_question, disabled=not style)
    
    elif st.session_state.question_stage == 5:
        st.header("Q5: 月額予算を教えてください")
        
        # 予算のステップを固定
        budget_options = [980, 1500, 2000, 3000, 4000, 5000, 6000]
        budget = st.select_slider(
            "1ヶ月あたりの予算（円）:",
            options=budget_options,
            value=3000,
            key="budget_slider_q5"
        )
        
        st.session_state.answers['budget'] = budget
        
        # ボタン配置
        col1, col2 = st.columns(2)
        with col1:
            st.button("戻る", key="back_q5", on_click=go_to_prev_question)
        with col2:
            st.button("次へ", type="primary", key="next_q5", on_click=go_to_next_question)
    
    elif st.session_state.question_stage == 6:
        st.header("Q6: 特に重視する機能はありますか？")
        
        feature_options = {
            "学習管理機能": "learning_management",
            "オンラインサポート": "online_support",
            "教科の充実度": "subject_variety",
            "問題量": "exercise_quantity",
            "双方向性": "interactive",
            "AI学習": "ai_learning",
            "思考力・論理的思考力養成": "thinking_skills",
            "コストパフォーマンスの良さ": "cost_effective",
            "動画授業の質と量": "video_lessons",
            "テスト対策の充実度": "test_preparation",
            "発展的な学習内容": "advanced_learning",
            "特別支援・学習サポート": "special_needs_support"
        }
        
        selected_features = st.multiselect(
            "重視する機能を選択してください（3つまで）:",
            options=list(feature_options.keys()),
            default=[],
            max_selections=3,
            key="features_multiselect_q6"
        )
        
        # 選択した機能を保存
        if selected_features:
            st.session_state.answers['features'] = [feature_options[feature] for feature in selected_features]
        else:
            st.session_state.answers['features'] = []
        
        # 結果表示への遷移関数
        def finish_questionnaire():
            # 簡易レコメンデーション（実際のプロジェクトではもっと複雑なロジック）
            recommendations = []
            budget = st.session_state.answers.get('budget', 3000)
            
            # 予算内の商品をフィルタリング
            for product in tablet_data:
                if product['monthly_fee'] <= budget:
                    recommendations.append(product['id'])
            
            # 結果を保存
            st.session_state.recommendations = recommendations[:3]
            st.session_state.page = 'results'
        
        # ボタン配置
        col1, col2 = st.columns(2)
        with col1:
            st.button("戻る", key="back_q6", on_click=go_to_prev_question)
        with col2:
            st.button("診断結果を見る", type="primary", key="finish_q6", on_click=finish_questionnaire)

elif st.session_state.page == 'results':
    st.title("🎯 診断結果")
    
    if not st.session_state.recommendations:
        st.error("診断結果がありません。診断をやり直してください。")
        st.button("診断に戻る", key="results_back_to_quiz", on_click=go_to_questionnaire)
    else:
        st.write("お子様の情報に基づく、おすすめのタブレット教材です")
        
        # 推奨タブレット教材の表示（シンプルバージョン）
        for i, rec_id in enumerate(st.session_state.recommendations[:3]):
            product = next((p for p in tablet_data if p['id'] == rec_id), None)
            if not product:
                continue
                
            st.subheader(f"{i+1}. {product['name']}")
            
            # 基本情報
            cols = st.columns(3)
            with cols[0]:
                st.write(f"**月額**: {product['monthly_fee']}円")
            with cols[1]:
                st.write(f"**初期費用**: {product['initial_fee']}円")
            with cols[2]:
                st.write(f"[詳細情報]({product['url']})")
            
            # 商品説明
            st.write(f"**特徴**: {product['description']}")
            
            st.divider()
        
        # 診断のやり直し
        st.button("診断をやり直す", key="results_restart", on_click=go_to_questionnaire)

else:
    st.error("ページが見つかりません")
    st.button("ホームに戻る", key="error_home", on_click=go_to_home)