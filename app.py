import streamlit as st

# アプリの設定
st.set_page_config(
    page_title="子供のタブレット教材診断ツール",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# モバイル表示のためのCSS設定（タブを下部に表示）
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
</style>
""", unsafe_allow_html=True)

# 基本的なデータ（最適化版）
tablet_basic_data = [
    {
        "id": "challenge_touch",
        "name": "チャレンジタッチ",
        "monthly_fee": 3250,  # 小1～2年生の場合（12ヶ月一括払い）
        "initial_fee": 0,  # 6ヶ月未満退会時はタブレット代8,300円が必要
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary"],
        "subjects": ["japanese", "math", "english", "science", "social", "programming"],
        "strengths": [
            "豊富な動画と音声による解説",
            "初期費用0円・専用タブレット付き",
            "紙教材との併用で効果的"
        ],
        "weaknesses": [
            "学力向上効果は平均的",
            "基礎固めが中心で応用力を伸ばすには不向き"
        ],
        "description": "ベネッセの「進研ゼミ」のタブレット版で、基礎力養成を目的とした質の高い学習コンテンツと、専用タブレットが提供されます。",
        "url": "https://jinzaikachi.com/challenge-campaign/",
        "features": ["learning_management", "subject_variety", "online_support", "exercise_quantity"],
        "ratings": {
            "cost_performance": 7,
            "learning_effect": 8,
            "curriculum": 9,
            "usability": 8,
            "support": 9,
            "motivation": 7
        }
    },
    {
        "id": "smile_zemi",
        "name": "スマイルゼミ",
        "monthly_fee": 3278,  # 小1～2年生の場合（12ヶ月一括払い）
        "initial_fee": 0,  # 6ヶ月未満退会時はタブレット代32,802円が必要
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary"],
        "subjects": ["japanese", "math", "english", "science", "social", "programming"],
        "strengths": [
            "全科目対応でバランス良く学べる",
            "AIが得意・苦手を分析して出題",
            "丁寧な解説とステップアップ学習"
        ],
        "weaknesses": [
            "専用タブレットの初期費用が必要",
            "学習内容は基礎力養成が中心"
        ],
        "description": "スマイルゼミは、幼児から中学生まで対応した総合的なタブレット教材です。AIが子どもの理解度に合わせて問題を出題します。",
        "url": "https://jinzaikachi.com/smilezemi-campaign/",
        "features": ["learning_management", "subject_variety", "exercise_quantity", "ai_learning"],
        "ratings": {
            "cost_performance": 6,
            "learning_effect": 8,
            "curriculum": 9,
            "usability": 9,
            "support": 8,
            "motivation": 8
        }
    },
    {
        "id": "z_kai_tablet",
        "name": "Z会タブレットコース",
        "monthly_fee": 3570,  # 小1年生の場合（12ヶ月一括払い）
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary"],
        "subjects": ["japanese", "math", "english", "science", "social", "programming", "thinking"],
        "strengths": [
            "思考力・記述力を重視したカリキュラム",
            "難関中学受験対策に効果的",
            "先取り学習が可能"
        ],
        "weaknesses": [
            "教材ボリュームが多くて大変",
            "難易度が高く挫折リスクがある"
        ],
        "description": "Z会タブレットコースは、思考力・表現力を重視した難関校受験にも対応する高品質な学習教材です。",
        "url": "https://jinzaikachi.com/z-tablet/",
        "features": ["subject_variety", "exercise_quantity", "learning_management", "thinking_skills"],
        "ratings": {
            "cost_performance": 5,
            "learning_effect": 9,
            "curriculum": 10,
            "usability": 7,
            "support": 7,
            "motivation": 6
        }
    },
    {
        "id": "risu_kids",
        "name": "RISU算数",
        "monthly_fee": 2948,  # 基本料金＋利用料が発生（進度に応じて変動）
        "initial_fee": 0,
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary"],
        "subjects": ["math"],
        "strengths": [
            "AIによる進度調整と個別対応",
            "つまずき箇所を徹底的に克服",
            "自分のペースで先取り学習可能"
        ],
        "weaknesses": [
            "算数のみの対応で他教科は別途必要",
            "子ども向けキャラクターなど親しみ要素が少ない"
        ],
        "description": "RISU算数は、AIが子どもの理解度を精密に分析し、一人ひとりに最適な問題を提供する算数特化型のタブレット教材です。",
        "url": "https://jinzaikachi.com/risu-math/",
        "features": ["ai_learning", "exercise_quantity", "interactive"],
        "ratings": {
            "cost_performance": 7,
            "learning_effect": 9,
            "curriculum": 8,
            "usability": 8,
            "support": 6,
            "motivation": 7
        }
    },
    {
        "id": "study_suppli",
        "name": "スタディサプリ小学講座",
        "monthly_fee": 1815,  # 学年が上がっても定額
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "strengths": [
            "リーズナブルな料金設定",
            "実績のある講師陣による動画授業",
            "自分のペースで繰り返し視聴可能"
        ],
        "weaknesses": [
            "AIによる個別最適化機能は弱い",
            "学習管理は保護者主導になりがち"
        ],
        "description": "スタディサプリ小学講座は、有名講師による質の高い授業動画と演習問題を低価格で利用できるオンライン学習サービスです。",
        "url": "https://jinzaikachi.com/study-supple/",
        "features": ["video_lessons", "exercise_quantity", "learning_management", "cost_effective"],
        "ratings": {
            "cost_performance": 9,
            "learning_effect": 7,
            "curriculum": 8,
            "usability": 8,
            "support": 6,
            "motivation": 7
        }
    },
    {
        "id": "toshin_online",
        "name": "東進オンライン学校（小学部）",
        "monthly_fee": 2178,  # 小1～2年生の場合
        "initial_fee": 0,
        "grade_range": ["upper_elementary"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "strengths": [
            "難関中学受験に強い指導カリキュラム",
            "一流講師陣による授業で難関校合格実績あり",
            "志望校に合わせた学習プラン"
        ],
        "weaknesses": [
            "月額費用が高め",
            "難易度が高く基礎固めには不向き"
        ],
        "description": "東進オンライン学校は難関中学受験を目指す小学生のための本格的なオンライン学習塾です。",
        "url": "https://jinzaikachi.com/toushin-online-syougakubu/",
        "features": ["video_lessons", "exercise_quantity", "test_preparation", "advanced_learning"],
        "ratings": {
            "cost_performance": 4,
            "learning_effect": 9,
            "curriculum": 9,
            "usability": 7,
            "support": 7,
            "motivation": 5
        }
    },
    {
        "id": "dekitasu",
        "name": "デキタス",
        "monthly_fee": 3960,  # 学年が上がっても定額
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "strengths": [
            "AIによる個別学習プラン作成",
            "子どもが楽しく続けられるゲーム要素",
            "リーズナブルな料金設定"
        ],
        "weaknesses": [
            "思考力や記述力を鍛える問題は少なめ",
            "キャラクター要素が多く集中力が散漫になる場合も"
        ],
        "description": "デキタスは、ゲーム要素を取り入れた楽しい学習体験と、AIによる個別最適化学習を組み合わせたタブレット教材です。",
        "url": "https://jinzaikachi.com/dekitasu/",
        "features": ["ai_learning", "exercise_quantity", "learning_management", "interactive"],
        "ratings": {
            "cost_performance": 8,
            "learning_effect": 7,
            "curriculum": 7,
            "usability": 9,
            "support": 7,
            "motivation": 9
        }
    },
    {
        "id": "poppy",
        "name": "小学ポピー",
        "monthly_fee": 2980,  # 小1～2年生の場合
        "initial_fee": 0,
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "strengths": [
            "非常にリーズナブルな料金設定",
            "学校の教科書に準拠した内容",
            "テスト対策にも役立つ基礎力養成"
        ],
        "weaknesses": [
            "応用力や思考力を鍛える内容は少なめ",
            "AIによる個別最適化機能はない"
        ],
        "description": "小学ポピーは60年以上の実績を持つ通信教育で、基本はプリント学習ですが、タブレット学習も組み合わせることができます。",
        "url": "https://jinzaikachi.com/popi-campaign/",
        "features": ["exercise_quantity", "cost_effective", "paper_based"],
        "ratings": {
            "cost_performance": 10,
            "learning_effect": 6,
            "curriculum": 7,
            "usability": 8,
            "support": 6,
            "motivation": 6
        }
    },
    {
        "id": "substa",
        "name": "サブスタ",
        "monthly_fee": 980,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "strengths": [
            "業界最安クラスの月額料金",
            "わかりやすい授業動画",
            "定期テスト対策に効果的"
        ],
        "weaknesses": [
            "演習問題の量がやや少なめ",
            "個別最適化機能はない"
        ],
        "description": "サブスタは月額980円から利用できる低価格のオンライン学習サービスです。",
        "url": "https://jinzaikachi.com/sabusuta/",
        "features": ["video_lessons", "cost_effective", "test_preparation"],
        "ratings": {
            "cost_performance": 10,
            "learning_effect": 6,
            "curriculum": 7,
            "usability": 7,
            "support": 5,
            "motivation": 5
        }
    },
    {
        "id": "tenjin",
        "name": "天神",
        "monthly_fee": 2980,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "strengths": [
            "苦手科目の克服に特化",
            "学校の授業の遅れを取り戻せる",
            "基礎から丁寧に学び直せる"
        ],
        "weaknesses": [
            "応用力や発展的な内容は少なめ",
            "受験対策としては物足りない場合も"
        ],
        "description": "天神は学校の授業についていけない子どもや、苦手科目の克服を目的とした小中学生向けタブレット教材です。",
        "url": "https://jinzaikachi.com/tenjin/",
        "features": ["ai_learning", "exercise_quantity", "learning_management"],
        "ratings": {
            "cost_performance": 7,
            "learning_effect": 7,
            "curriculum": 7,
            "usability": 8,
            "support": 7,
            "motivation": 6
        }
    },
    {
        "id": "marugland",
        "name": "まるぐランド for HOME",
        "monthly_fee": 1078,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary"],
        "subjects": ["japanese", "math"],
        "strengths": [
            "特別支援教育の知見を活かした教材",
            "学習につまずきがある子にも効果的",
            "基礎から丁寧に学べる"
        ],
        "weaknesses": [
            "国語と算数のみの対応",
            "教科書対応ではなく基礎スキル重視"
        ],
        "description": "まるぐランド for HOMEは、特別支援教育の知見を活かした、つまずきのある子どもにも優しい学習教材です。",
        "url": "https://jinzaikachi.com/marug-campaign/",
        "features": ["ai_learning", "exercise_quantity", "special_needs_support"],
        "ratings": {
            "cost_performance": 9,
            "learning_effect": 7,
            "curriculum": 6,
            "usability": 8,
            "support": 9,
            "motivation": 7
        }
    },
    {
        "id": "surara",
        "name": "すらら",
        "monthly_fee": 4378,
        "initial_fee": 11000,
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "strengths": [
            "わかりやすいアニメーション授業",
            "つまずきに合わせた個別カリキュラム",
            "特別支援教育の知見を活用"
        ],
        "weaknesses": [
            "月額費用と初期費用が高め",
            "アニメーション中心で実写講師の授業はない"
        ],
        "description": "すららは学校でも多く導入されている、つまずき診断と個別最適化学習が特徴のタブレット教材です。",
        "url": "https://jinzaikachi.com/surara/",
        "features": ["ai_learning", "exercise_quantity", "learning_management", "special_needs_support"],
        "ratings": {
            "cost_performance": 5,
            "learning_effect": 8,
            "curriculum": 8,
            "usability": 9,
            "support": 9,
            "motivation": 8
        }
    },
    {
        "id": "logic_labo",
        "name": "ロジックラボ",
        "monthly_fee": 1980,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary"],
        "subjects": ["math", "programming", "thinking"],
        "strengths": [
            "論理的思考力や数理能力を鍛える",
            "楽しみながら思考力が身につく",
            "AI、プログラミング的思考の基礎を培う"
        ],
        "weaknesses": [
            "教科学習ではなく思考力トレーニング中心",
            "学校の成績向上に直結しにくい"
        ],
        "description": "ロジックラボは数理能力と論理的思考力を楽しく鍛える教材です。将来のAI時代に必要な思考力の基礎を育みます。",
        "url": "https://jinzaikachi.com/rogiqlabo/",
        "features": ["thinking_skills", "exercise_quantity", "programming_education"],
        "ratings": {
            "cost_performance": 8,
            "learning_effect": 6,
            "curriculum": 7,
            "usability": 8,
            "support": 6,
            "motivation": 9
        }
    },
    {
        "id": "wonder_box",
        "name": "ワンダーボックス",
        "monthly_fee": 2980,
        "initial_fee": 0,
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary"],
        "subjects": ["thinking", "programming", "science", "art"],
        "strengths": [
            "創造力と思考力を育む多彩なプロジェクト",
            "実験キットとタブレット学習の組み合わせ",
            "STEAM教育で未来の力を養う"
        ],
        "weaknesses": [
            "教科学習ではなく総合的な能力開発",
            "学校の成績向上に直結しにくい"
        ],
        "description": "ワンダーボックスは毎月届く実験キットとタブレット学習を組み合わせた、創造力と思考力を育むSTEAM教育教材です。",
        "url": "https://jinzaikachi.com/wonderbox/",
        "features": ["thinking_skills", "creativity", "stem_education", "project_based"],
        "ratings": {
            "cost_performance": 6,
            "learning_effect": 5,
            "curriculum": 8,
            "usability": 7,
            "support": 6,
            "motivation": 10
        }
    },
    {
        "id": "groovy_lab",
        "name": "グルービーラボ イン ア ボックス",
        "monthly_fee": 2980,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary"],
        "subjects": ["science", "engineering", "art", "math"],
        "strengths": [
            "本格的な科学実験が家庭でできる",
            "タブレットと実物教材の組み合わせ",
            "実験を通じて科学的思考力を養う"
        ],
        "weaknesses": [
            "教科学習ではなく体験型学習が中心",
            "学校の成績向上に直結しにくい"
        ],
        "description": "グルービーラボは米国発の科学教材で、毎月テーマの異なる実験キットとタブレット解説で、楽しく科学を学べます。",
        "url": "https://jinzaikachi.com/groovy/",
        "features": ["thinking_skills", "creativity", "stem_education", "project_based"],
        "ratings": {
            "cost_performance": 6,
            "learning_effect": 6,
            "curriculum": 7,
            "usability": 7,
            "support": 5,
            "motivation": 10
        }
    }
]

# パフォーマンス指標の定義
performance_indicators = {
    "cost_performance": {"name": "コスパ", "description": "料金設定とサービス内容のバランス"},
    "learning_effect": {"name": "学習効果", "description": "基礎的な学力向上効果"},
    "curriculum": {"name": "カリキュラム", "description": "学習内容の充実度と順序立て"},
    "usability": {"name": "使いやすさ", "description": "操作性と直感的な理解のしやすさ"},
    "support": {"name": "サポート", "description": "保護者向け機能や学習サポート"},
    "motivation": {"name": "継続性", "description": "楽しく続けられる工夫"}
}

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

# 最適化された推薦アルゴリズム
def get_optimized_recommendations(answers):
    # ポイント計算のための辞書
    product_points = {product['id']: 0 for product in tablet_basic_data}
    
    # 予算フィルタリング
    budget = answers.get('budget', 10000)
    for product in tablet_basic_data:
        if product['monthly_fee'] <= budget:
            # 予算内なら加点
            product_points[product['id']] += 10
            
            # 予算の70-90%の範囲内ならさらに加点
            if product['monthly_fee'] >= budget * 0.7 and product['monthly_fee'] <= budget * 0.9:
                product_points[product['id']] += 5
        else:
            # 予算オーバーなら大幅減点
            product_points[product['id']] -= 50
    
    # 学年マッチング
    grade = answers.get('grade')
    if grade:
        for product in tablet_basic_data:
            if grade in product['grade_range']:
                product_points[product['id']] += 10
            else:
                product_points[product['id']] -= 30
    
    # 科目マッチング
    subjects = answers.get('subjects', [])
    if subjects:
        for product in tablet_basic_data:
            matched_subjects = set(subjects) & set(product['subjects'])
            product_points[product['id']] += len(matched_subjects) * 5
    
    # 目的マッチング
    purpose = answers.get('purpose')
    if purpose:
        purpose_product_match = {
            'catch_up': ['study_suppli', 'tenjin', 'marugland', 'substa'],
            'habit_formation': ['challenge_touch', 'smile_zemi', 'dekitasu', 'poppy'],
            'exam_preparation': ['z_kai_tablet', 'toshin_online', 'study_suppli'],
            'weakness_improvement': ['risu_kids', 'tenjin', 'marugland', 'surara'],
            'advanced_learning': ['z_kai_tablet', 'risu_kids', 'toshin_online'],
            'thinking_creativity': ['logic_labo', 'wonder_box', 'groovy_lab', 'z_kai_tablet']
        }
        
        if purpose in purpose_product_match:
            for product_id in purpose_product_match[purpose]:
                product_points[product_id] += 15
    
    # 学習スタイルマッチング
    style = answers.get('learning_style')
    if style:
        style_product_match = {
            'video_learning': ['study_suppli', 'toshin_online', 'substa'],
            'gamified_learning': ['dekitasu', 'logic_labo', 'wonder_box'],
            'self_paced': ['risu_kids', 'z_kai_tablet', 'tenjin'],
            'experiential_learning': ['wonder_box', 'groovy_lab'],
            'ai_adaptive': ['risu_kids', 'smile_zemi', 'dekitasu', 'surara'],
            'hybrid_learning': ['challenge_touch', 'poppy', 'z_kai_tablet']
        }
        
        if style in style_product_match:
            for product_id in style_product_match[style]:
                product_points[product_id] += 15
    
    # 特徴マッチング
    features = answers.get('features', [])
    if features:
        for product in tablet_basic_data:
            matched_features = set(features) & set(product['features'])
            product_points[product['id']] += len(matched_features) * 8
    
    # 結果をソート
    sorted_products = sorted(product_points.items(), key=lambda x: x[1], reverse=True)
    return [product_id for product_id, points in sorted_products if points > 0]

# サイドバー（シンプル）
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
    st.title("🎓 子供のタブレット教材診断ツール")
    
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
            
            # ボタンクリックで次のステージに進める
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
            
            # 選択後もボタンで操作できるように
            col1, col2 = st.columns(2)
            with col1:
                if st.button("戻る", key="back_q2"):
                    st.session_state.question_stage = 1
            with col2:
                if st.button("次へ", type="primary", key="next_q2"):
                    st.session_state.question_stage = 3
        else:
            # 科目が選択されていない場合は、ボタンを表示
            col1, col2 = st.columns(2)
            with col1:
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
            
            # ボタンで操作できるように設定
            col1, col2 = st.columns(2)
            with col1:
                if st.button("戻る", key="back_q3"):
                    st.session_state.question_stage = 2
            with col2:
                if st.button("次へ", type="primary", key="next_q3"):
                    st.session_state.question_stage = 4
        else:
            # 目的が選択されていない場合は、ボタンを表示
            col1, col2 = st.columns(2)
            with col1:
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
            
            # クリック可能なボタンで操作
            col1, col2 = st.columns(2)
            with col1:
                if st.button("戻る", key="back_q4"):
                    st.session_state.question_stage = 3
            with col2:
                if st.button("次へ", type="primary", key="next_q4"):
                    st.session_state.question_stage = 5
        else:
            # 学習スタイルが選択されていない場合は、ボタンを表示
            col1, col2 = st.columns(2)
            with col1:
                if st.button("戻る", key="back_q4_nostyle"):
                    st.session_state.question_stage = 3
    
    # 質問5: 予算
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
        
        # 通常のボタンで操作
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
            
        # 通常のボタン操作で診断結果に進む
        col1, col2 = st.columns(2)
        with col1:
            if st.button("戻る", key="back_q6"):
                st.session_state.question_stage = 5
        with col2:
            if st.button("診断結果を見る", type="primary", key="finish_q6"):
                # 推薦アルゴリズムを実行
                recommendations = get_optimized_recommendations(st.session_state.answers)
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
                'upper_elementary': '小学校高学年'
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
        
        # 推奨タブレット教材の表示（最適化バージョン）
        for i, rec_id in enumerate(st.session_state.recommendations[:5]):  # 上位5件表示
            product = next((p for p in tablet_basic_data if p['id'] == rec_id), None)
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
            
            # 強みと弱み
            with st.expander("強みと弱み", expanded=False):
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**強み**")
                    for strength in product['strengths']:
                        st.write(f"✅ {strength}")
                with col2:
                    st.write("**弱み**")
                    for weakness in product['weaknesses']:
                        st.write(f"⚠️ {weakness}")
            
            # パフォーマンス指標（シンプル化）
            with st.expander("パフォーマンス指標", expanded=False):
                for perf_key, perf_info in performance_indicators.items():
                    rating = product['ratings'].get(perf_key, 0)
                    
                    # 評価によって色分け
                    if rating >= 8:
                        color = "🟢"  # 良い - 緑
                    elif rating >= 6:
                        color = "🟡"  # 普通 - 黄色
                    else:
                        color = "🔴"  # 改善の余地あり - 赤
                    
                    st.write(f"**{perf_info['name']}**: {color} {rating}/10")
            
            st.divider()
        
        # 診断のやり直し
        if st.button("診断をやり直す", key="results_restart"):
            reset_session()
            go_to_questionnaire()

else:
    st.error("ページが見つかりません")
    if st.button("ホームに戻る", key="error_home"):
        go_to_home()