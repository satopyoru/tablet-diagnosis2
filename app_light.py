import streamlit as st
from data import tablet_data, tablet_urls, product_performance, performance_indicators

# アプリの設定
st.set_page_config(
    page_title="子供のタブレット教材診断ツール（軽量版）",
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

# ナビゲーション関数
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

# サイドバー（シンプル化）
with st.sidebar:
    st.title("メニュー")
    
    if st.button("ホーム", key="sidebar_home"):
        go_to_home()
    
    if st.button("診断スタート", key="sidebar_start"):
        go_to_questionnaire()
    
    if st.button("診断結果", key="sidebar_results"):
        go_to_results()
    
    st.divider()
    if st.button("リセット", key="sidebar_reset"):
        reset_session()

# メインコンテンツ
if st.session_state.page == 'home':
    st.title("🎓 子供のタブレット教材診断ツール（軽量版）")
    
    st.markdown("""
    ### お子様に最適なタブレット教材を見つけましょう
    
    このツールでは、お子様の学年、興味のある科目、ご予算などに基づいて、
    最適なタブレット教材をご提案します。
    
    多くの選択肢があり、どれを選べばよいのか迷っている保護者の方々をサポートします。
    
    ### 使い方
    1. 「診断スタート」をクリックして質問に答えてください
    2. お子様のニーズに合わせた教材をご提案します
    
    さあ、始めましょう！
    """)
    
    if st.button("診断を始める", use_container_width=True, type="primary", key="home_start"):
        go_to_questionnaire()

elif st.session_state.page == 'questionnaire':
    st.title("📝 お子様に最適な教材を見つけるための診断")
    
    # プログレスバーの表示
    progress = st.session_state.question_stage / 6
    st.progress(progress)
    st.write(f"ステップ {st.session_state.question_stage}/6")
    
    # 質問1: 学年
    if st.session_state.question_stage == 1:
        st.header("Q1: お子様の学年を教えてください")
        
        grade = st.radio(
            "学年を選択してください:",
            options=[
                "幼児（年少・年中・年長）",
                "小学校低学年（1〜3年生）",
                "小学校高学年（4〜6年生）"
            ],
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
            
            col1, col2 = st.columns(2)
            with col2:
                if st.button("次へ", type="primary", key="next_q1"):
                    st.session_state.question_stage = 2
    
    # 質問2: 科目
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
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("戻る", key="back_q2"):
                    st.session_state.question_stage = 1
            with col2:
                if st.button("次へ", type="primary", key="next_q2"):
                    st.session_state.question_stage = 3
        else:
            if st.button("戻る", key="back_q2_nosub"):
                st.session_state.question_stage = 1
    
    # 質問3: 学習の目的
    elif st.session_state.question_stage == 3:
        st.header("Q3: 学習の主な目的は何ですか？")
        
        purpose = st.radio(
            "最も当てはまるものを選んでください:",
            options=[
                "学校の授業についていくため",
                "学習習慣を身につけるため",
                "中学受験の準備のため",
                "苦手科目を克服するため",
                "先取り学習・発展学習のため",
                "思考力・創造性を伸ばすため"
            ],
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
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("戻る", key="back_q3"):
                    st.session_state.question_stage = 2
            with col2:
                if st.button("次へ", type="primary", key="next_q3"):
                    st.session_state.question_stage = 4
        else:
            if st.button("戻る", key="back_q3_nopurpose"):
                st.session_state.question_stage = 2
    
    # 質問4: 学習スタイル
    elif st.session_state.question_stage == 4:
        st.header("Q4: お子様の好みの学習スタイルは？")
        
        style = st.radio(
            "最も当てはまるものを選んでください:",
            options=[
                "動画授業で学ぶのが好き",
                "ゲーム感覚で楽しく学びたい",
                "自分のペースでコツコツ取り組みたい",
                "実験や体験を通して学びたい",
                "AIが個別対応してくれる学習がいい",
                "紙とデジタルの両方を使った学習がいい"
            ],
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
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("戻る", key="back_q4"):
                    st.session_state.question_stage = 3
            with col2:
                if st.button("次へ", type="primary", key="next_q4"):
                    st.session_state.question_stage = 5
        else:
            if st.button("戻る", key="back_q4_nostyle"):
                st.session_state.question_stage = 3
    
    # 質問5: 予算
    elif st.session_state.question_stage == 5:
        st.header("Q5: 月額予算を教えてください")
        
        # 予算値を正規化して、stepに合うようにする
        current_budget = st.session_state.answers.get('budget', 3000)
        # 500の倍数に調整
        normalized_budget = (current_budget // 500) * 500
        if normalized_budget < 980:
            normalized_budget = 980
            
        budget = st.slider(
            "1ヶ月あたりの予算（円）:",
            min_value=980,
            max_value=9000,
            value=normalized_budget,
            step=500,
            key="budget_slider_q5"
        )
        
        st.session_state.answers['budget'] = budget
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("戻る", key="back_q5"):
                st.session_state.question_stage = 4
        with col2:
            if st.button("次へ", type="primary", key="next_q5"):
                st.session_state.question_stage = 6
    
    # 質問6: 重視する機能
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
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("戻る", key="back_q6"):
                st.session_state.question_stage = 5
        with col2:
            if st.button("診断結果を見る", type="primary", key="finish_q6"):
                # 推薦アルゴリズムを実行
                from recommendation import get_recommendations
                recommendations = get_recommendations(st.session_state.answers)
                st.session_state.recommendations = recommendations
                st.session_state.page = 'results'

elif st.session_state.page == 'results':
    st.title("🎯 診断結果")
    
    if not st.session_state.recommendations:
        st.error("診断結果がありません。診断をやり直してください。")
        if st.button("診断に戻る", key="results_back_to_quiz"):
            go_to_questionnaire()
    else:
        st.write("お子様の情報に基づく、おすすめのタブレット教材です")
        
        # 回答サマリー
        with st.expander("あなたの回答", expanded=False):
            grade_mapping = {
                'kindergarten': '幼児',
                'lower_elementary': '小学校低学年',
                'upper_elementary': '小学校高学年',
                'junior_high': '中学生'
            }
            st.write(f"**学年**: {grade_mapping.get(st.session_state.answers['grade'], '')}")
            st.write(f"**月額予算**: {st.session_state.answers['budget']}円")
        
            subject_mapping = {
                'japanese': '国語',
                'math': '算数/数学',
                'english': '英語',
                'science': '理科',
                'social': '社会',
                'programming': 'プログラミング',
                'thinking': '思考力・論理的思考',
                'art': 'アート・創造性',
                'comprehensive': '総合学習',
                'engineering': '工学'
            }
            subjects = [subject_mapping.get(s, s) for s in st.session_state.answers['subjects']]
            st.write(f"**学習したい科目**: {', '.join(subjects)}")
            
            purpose_mapping = {
                'catch_up': '学校の授業についていくため',
                'habit_formation': '学習習慣を身につけるため',
                'exam_preparation': '中学受験の準備のため',
                'weakness_improvement': '苦手科目を克服するため',
                'advanced_learning': '先取り学習・発展学習のため',
                'thinking_creativity': '思考力・創造性を伸ばすため'
            }
            if st.session_state.answers.get('purpose'):
                st.write(f"**学習の目的**: {purpose_mapping.get(st.session_state.answers['purpose'], '')}")
            
            style_mapping = {
                'video_learning': '動画授業で学ぶのが好き',
                'gamified_learning': 'ゲーム感覚で楽しく学びたい',
                'self_paced': '自分のペースでコツコツ取り組みたい',
                'experiential_learning': '実験や体験を通して学びたい',
                'ai_adaptive': 'AIが個別対応してくれる学習がいい',
                'hybrid_learning': '紙とデジタルの両方を使った学習がいい'
            }
            if st.session_state.answers.get('learning_style'):
                st.write(f"**学習スタイル**: {style_mapping.get(st.session_state.answers['learning_style'], '')}")
            
            feature_mapping = {
                'learning_management': '学習管理機能',
                'online_support': 'オンラインサポート',
                'subject_variety': '教科の充実度',
                'exercise_quantity': '問題量',
                'interactive': '双方向性',
                'ai_learning': 'AI学習',
                'thinking_skills': '思考力・論理的思考力養成',
                'cost_effective': 'コストパフォーマンスの良さ',
                'video_lessons': '動画授業の質と量',
                'test_preparation': 'テスト対策の充実度',
                'advanced_learning': '発展的な学習内容',
                'special_needs_support': '特別支援・学習サポート',
                'creativity': '創造性を育む内容',
                'stem_education': 'STEM教育',
                'project_based': 'プロジェクト型学習'
            }
            features = [feature_mapping.get(f, f) for f in st.session_state.answers['features']]
            st.write(f"**重視する機能**: {', '.join(features)}")
        
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
                product_url = tablet_urls.get(product['id'], "#")
                st.write(f"[詳細情報]({product_url})")
            
            # 商品説明
            st.write(f"**特徴**: {product['description']}")
            
            # 強みと弱み（簡略化）
            exp = st.expander("強みと弱み", expanded=False)
            with exp:
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**強み**")
                    for strength in product['strengths']:
                        st.write(f"✅ {strength}")
                with col2:
                    st.write("**弱み**")
                    for weakness in product['weaknesses']:
                        st.write(f"⚠️ {weakness}")
            
            # パフォーマンス指標（簡略化）
            st.write("**パフォーマンス指標**:")
            perf_cols = st.columns(3)
            product_id = product['id']
            perf_ratings = product_performance.get(product_id, {})
            
            for idx, (perf_key, perf_info) in enumerate(performance_indicators.items()):
                col_idx = idx % 3
                rating = perf_ratings.get(perf_key, 0)
                
                # 評価によって色分け
                if rating >= 8:
                    color = "🟢"  # 良い - 緑
                    text_color = "green"
                elif rating >= 6:
                    color = "🟡"  # 普通 - 黄色
                    text_color = "orange"
                else:
                    color = "🔴"  # 改善の余地あり - 赤
                    text_color = "red"
                
                with perf_cols[col_idx]:
                    st.markdown(f"**{perf_info['name']}**: <span style='color:{text_color}'>{color} {rating}/10</span>", unsafe_allow_html=True)
            
            st.divider()
        
        # 診断のやり直し
        if st.button("診断をやり直す", key="results_restart"):
            reset_session()
            go_to_questionnaire()

else:
    st.error("ページが見つかりません")
    if st.button("ホームに戻る", key="error_home"):
        go_to_home()