import streamlit as st

# アプリの設定
st.set_page_config(
    page_title="子供のタブレット教材診断ツール（超軽量版）",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 基本的なデータ（最小限）
tablet_basic_data = [
    {
        "id": "challenge_touch",
        "name": "チャレンジタッチ",
        "monthly_fee": 3250,
        "initial_fee": 0,
        "description": "ベネッセの「進研ゼミ」のタブレット版で、基礎力養成を目的とした質の高い学習コンテンツと、専用タブレットが提供されます。",
        "url": "https://jinzaikachi.com/challenge-campaign/"
    },
    {
        "id": "smile_zemi",
        "name": "スマイルゼミ",
        "monthly_fee": 3278,
        "initial_fee": 11000,
        "description": "スマイルゼミは、幼児から中学生まで対応した総合的なタブレット教材です。AIが子どもの理解度に合わせて問題を出題します。",
        "url": "https://jinzaikachi.com/smilezemi-campaign/"
    },
    {
        "id": "z_kai_tablet",
        "name": "Z会タブレットコース",
        "monthly_fee": 3570,
        "initial_fee": 0,
        "description": "Z会タブレットコースは、思考力・表現力を重視した難関校受験にも対応する高品質な学習教材です。",
        "url": "https://jinzaikachi.com/z-tablet/"
    },
    {
        "id": "risu_kids",
        "name": "RISU算数",
        "monthly_fee": 2980,
        "initial_fee": 0,
        "description": "RISU算数は、AIが子どもの理解度を精密に分析し、一人ひとりに最適な問題を提供する算数特化型のタブレット教材です。",
        "url": "https://jinzaikachi.com/risu-math/"
    },
    {
        "id": "study_suppli",
        "name": "スタディサプリ小学講座",
        "monthly_fee": 2178,
        "initial_fee": 0,
        "description": "スタディサプリ小学講座は、有名講師による質の高い授業動画と演習問題を低価格で利用できるオンライン学習サービスです。",
        "url": "https://jinzaikachi.com/study-supple/"
    },
    {
        "id": "toshin_online",
        "name": "東進オンライン学校（小学部）",
        "monthly_fee": 5500,
        "initial_fee": 0,
        "description": "東進オンライン学校は難関中学受験を目指す小学生のための本格的なオンライン学習塾です。",
        "url": "https://jinzaikachi.com/toushin-online-syougakubu/"
    },
    {
        "id": "dekitasu",
        "name": "デキタス",
        "monthly_fee": 2178,
        "initial_fee": 0,
        "description": "デキタスは、ゲーム要素を取り入れた楽しい学習体験と、AIによる個別最適化学習を組み合わせたタブレット教材です。",
        "url": "https://jinzaikachi.com/dekitasu/"
    },
    {
        "id": "poppy",
        "name": "小学ポピー",
        "monthly_fee": 1400,
        "initial_fee": 0,
        "description": "小学ポピーは60年以上の実績を持つ通信教育で、基本はプリント学習ですが、タブレット学習も組み合わせることができます。",
        "url": "https://jinzaikachi.com/popi-campaign/"
    },
    {
        "id": "substa",
        "name": "サブスタ",
        "monthly_fee": 980,
        "initial_fee": 0,
        "description": "サブスタは月額980円から利用できる低価格のオンライン学習サービスです。",
        "url": "https://jinzaikachi.com/sabusuta/"
    },
    {
        "id": "tenjin",
        "name": "天神",
        "monthly_fee": 2980,
        "initial_fee": 0,
        "description": "天神は学校の授業についていけない子どもや、苦手科目の克服を目的とした小中学生向けタブレット教材です。",
        "url": "https://jinzaikachi.com/tenjin/"
    },
    {
        "id": "marugland",
        "name": "まるぐランド for HOME",
        "monthly_fee": 1078,
        "initial_fee": 0,
        "description": "まるぐランド for HOMEは、特別支援教育の知見を活かした、つまずきのある子どもにも優しい学習教材です。",
        "url": "https://jinzaikachi.com/marug-campaign/"
    },
    {
        "id": "surara",
        "name": "すらら",
        "monthly_fee": 4378,
        "initial_fee": 11000,
        "description": "すららは学校でも多く導入されている、つまずき診断と個別最適化学習が特徴のタブレット教材です。",
        "url": "https://jinzaikachi.com/surara/"
    },
    {
        "id": "logic_labo",
        "name": "ロジックラボ",
        "monthly_fee": 1980,
        "initial_fee": 0,
        "description": "ロジックラボは数理能力と論理的思考力を楽しく鍛える教材です。将来のAI時代に必要な思考力の基礎を育みます。",
        "url": "https://jinzaikachi.com/rogiqlabo/"
    },
    {
        "id": "wonder_box",
        "name": "ワンダーボックス",
        "monthly_fee": 2980,
        "initial_fee": 0,
        "description": "ワンダーボックスは毎月届く実験キットとタブレット学習を組み合わせた、創造力と思考力を育むSTEAM教育教材です。",
        "url": "https://jinzaikachi.com/wonderbox/"
    },
    {
        "id": "groovy_lab",
        "name": "グルービーラボ イン ア ボックス",
        "monthly_fee": 2980,
        "initial_fee": 0,
        "description": "グルービーラボは米国発の科学教材で、毎月テーマの異なる実験キットとタブレット解説で、楽しく科学を学べます。",
        "url": "https://jinzaikachi.com/groovy/"
    }
]

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
        'features': []
    }

if 'recommendations' not in st.session_state:
    st.session_state.recommendations = []

# ナビゲーション関数
def go_to_home():
    st.session_state.page = 'home'
    
def go_to_questionnaire():
    st.session_state.page = 'questionnaire'
    st.session_state.question_stage = 1

def reset_session():
    st.session_state.page = 'home'
    st.session_state.question_stage = 1
    st.session_state.answers = {
        'grade': None,
        'subjects': [],
        'budget': 3000,
        'features': []
    }
    st.session_state.recommendations = []

# 簡易推薦アルゴリズム
def get_simple_recommendations(answers):
    # 予算内の教材をフィルタリング
    budget = answers.get('budget', 10000)
    
    # 予算でフィルタリングした結果を返す（月額が予算以下）
    filtered_products = [p['id'] for p in tablet_basic_data if p['monthly_fee'] <= budget]
    
    # 予算に近い順（上限から見て70%以上）に並べ替え
    budget_threshold = budget * 0.7
    sorted_products = sorted(
        filtered_products,
        key=lambda pid: abs(next((p['monthly_fee'] for p in tablet_basic_data if p['id'] == pid), 0) - budget_threshold)
    )
    
    return sorted_products

# サイドバー（超シンプル）
with st.sidebar:
    st.title("メニュー")
    
    if st.button("ホーム", key="sidebar_home"):
        go_to_home()
    
    if st.button("診断スタート", key="sidebar_start"):
        go_to_questionnaire()
    
    st.divider()
    if st.button("リセット", key="sidebar_reset"):
        reset_session()

# メインコンテンツ
if st.session_state.page == 'home':
    st.title("🎓 子供のタブレット教材診断ツール（超軽量版）")
    
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
    progress = st.session_state.question_stage / 3  # 質問数を3に減らした
    st.progress(progress)
    st.write(f"ステップ {st.session_state.question_stage}/3")
    
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
    
    # 質問2: 科目（簡略化）
    elif st.session_state.question_stage == 2:
        st.header("Q2: 学習したい科目を選択してください")
        
        subject_options = {
            "国語": "japanese",
            "算数/数学": "math",
            "英語": "english",
            "理科": "science",
            "社会": "social",
            "プログラミング": "programming",
            "総合学習（複数科目）": "comprehensive"
        }
        
        selected_subjects = st.multiselect(
            "興味のある科目を選択してください（複数選択可）:",
            options=list(subject_options.keys()),
            default=[],
            key="subjects_multiselect_q2"
        )
        
        st.session_state.answers['subjects'] = [subject_options[subject] for subject in selected_subjects] if selected_subjects else []
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("戻る", key="back_q2"):
                st.session_state.question_stage = 1
        with col2:
            if st.button("次へ", type="primary", key="next_q2"):
                st.session_state.question_stage = 3
    
    # 質問3: 予算（最後の質問）
    elif st.session_state.question_stage == 3:
        st.header("Q3: 月額予算を教えてください")
        
        # 予算のステップを固定
        budget_options = [980, 1500, 2000, 3000, 4000, 5000, 6000]
        budget = st.select_slider(
            "1ヶ月あたりの予算（円）:",
            options=budget_options,
            value=3000,
            key="budget_slider_q3"
        )
        
        st.session_state.answers['budget'] = budget
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("戻る", key="back_q3"):
                st.session_state.question_stage = 2
        with col2:
            if st.button("診断結果を見る", type="primary", key="finish_q3"):
                # 簡易推薦アルゴリズムを実行
                recommendations = get_simple_recommendations(st.session_state.answers)
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
        
        # 回答サマリー（超シンプル）
        grade_mapping = {
            'kindergarten': '幼児',
            'lower_elementary': '小学校低学年',
            'upper_elementary': '小学校高学年'
        }
        
        st.write(f"**学年**: {grade_mapping.get(st.session_state.answers['grade'], '')}")
        st.write(f"**月額予算**: {st.session_state.answers['budget']}円")
        
        # 推奨タブレット教材の表示（超シンプル）
        for i, rec_id in enumerate(st.session_state.recommendations[:5]):  # 上位5件表示
            product = next((p for p in tablet_basic_data if p['id'] == rec_id), None)
            if not product:
                continue
                
            st.subheader(f"{i+1}. {product['name']}")
            
            # 基本情報
            st.write(f"**月額**: {product['monthly_fee']}円")
            st.write(f"**初期費用**: {product['initial_fee']}円")
            st.write(f"**特徴**: {product['description']}")
            st.write(f"[詳細情報]({product['url']})")
            
            st.divider()
        
        # 診断のやり直し
        if st.button("診断をやり直す", key="results_restart"):
            reset_session()
            go_to_questionnaire()

else:
    st.error("ページが見つかりません")
    if st.button("ホームに戻る", key="error_home"):
        go_to_home()