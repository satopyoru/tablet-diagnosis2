import streamlit as st
import pandas as pd
import plotly.express as px

from questionnaire import render_questionnaire
from comparison import render_comparison
from recommendation import get_recommendations
from data import tablet_data, tablet_urls, product_performance, performance_indicators

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

# ナビゲーション関数
def go_to_home():
    st.session_state.page = 'home'
    
def go_to_questionnaire():
    st.session_state.page = 'questionnaire'
    st.session_state.question_stage = 1
    
def go_to_comparison():
    st.session_state.page = 'comparison'
    
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

# サイドバー
with st.sidebar:
    st.title("メニュー")
    
    if st.button("ホーム", key="sidebar_home"):
        go_to_home()
    
    if st.button("診断スタート", key="sidebar_start"):
        go_to_questionnaire()
    
    if st.button("教材比較", key="sidebar_compare"):
        go_to_comparison()
    
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
    3. 「教材比較」で詳細な比較ができます
    
    さあ、始めましょう！
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("診断を始める", use_container_width=True, type="primary", key="home_start"):
            go_to_questionnaire()
    with col2:
        if st.button("教材を比較する", use_container_width=True, key="home_compare"):
            go_to_comparison()

elif st.session_state.page == 'questionnaire':
    render_questionnaire()

elif st.session_state.page == 'results':
    st.title("🎯 診断結果")
    
    if not st.session_state.recommendations:
        st.error("診断結果がありません。診断をやり直してください。")
        if st.button("診断に戻る", key="results_back_to_quiz"):
            go_to_questionnaire()
    else:
        st.write("お子様の情報に基づく、おすすめのタブレット教材です")
        
        # 回答サマリー
        with st.expander("あなたの回答", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                grade_mapping = {
                    'kindergarten': '幼児',
                    'lower_elementary': '小学校低学年',
                    'upper_elementary': '小学校高学年',
                    'junior_high': '中学生'
                }
                st.write(f"**学年**: {grade_mapping.get(st.session_state.answers['grade'], '')}")
                st.write(f"**月額予算**: {st.session_state.answers['budget']}円")
            
            with col2:
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
        
        # 推奨タブレット教材の表示
        for i, rec_id in enumerate(st.session_state.recommendations[:3]):
            product = next((p for p in tablet_data if p['id'] == rec_id), None)
            if not product:
                continue
                
            col1, col2 = st.columns([1, 3])
            with col1:
                product_url = tablet_urls.get(product['id'], "#")
                st.subheader(f"{i+1}. [{product['name']}]({product_url})")
                st.write(f"**月額**: {product['monthly_fee']}円")
                st.write(f"**初期費用**: {product['initial_fee']}円")
                match_score = product.get('match_score', 0)
                st.progress(match_score/100)
                st.write(f"マッチ度: {match_score}%")
                st.write(f"[詳細情報を見る]({product_url})")
            
            with col2:
                st.write(f"**特徴**: {product['description']}")
                
                # パフォーマンス指標の表示
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
                
                # 強みと弱みを表示
                col_a, col_b = st.columns(2)
                with col_a:
                    st.write("**強み**")
                    for strength in product['strengths']:
                        st.write(f"✅ {strength}")
                
                with col_b:
                    st.write("**弱み**")
                    for weakness in product['weaknesses']:
                        st.write(f"⚠️ {weakness}")
            
            st.divider()
            
        # 比較ボタン
        compare_ids = st.multiselect(
            "詳細に比較したい教材を選択してください",
            options=[p['id'] for p in tablet_data],
            default=st.session_state.recommendations[:2] if len(st.session_state.recommendations) >= 2 else st.session_state.recommendations,
            format_func=lambda x: next((p['name'] for p in tablet_data if p['id'] == x), x),
            key="results_compare_select"
        )
        
        if st.button("選択した教材を比較する", key="results_compare_button"):
            st.session_state['compare_ids'] = compare_ids
            go_to_comparison()
        
        # 共有機能
        with st.expander("結果を共有"):
            st.write("以下のテキストをコピーして共有できます:")
            
            share_text = f"""子供のタブレット教材診断結果:
学年: {grade_mapping.get(st.session_state.answers['grade'], '')}
学習目的: {', '.join(subjects)}
月額予算: {st.session_state.answers['budget']}円
重視する機能: {', '.join(features)}

おすすめ教材:
"""
            for i, rec_id in enumerate(st.session_state.recommendations[:3]):
                product = next((p for p in tablet_data if p['id'] == rec_id), None)
                if product:
                    product_url = tablet_urls.get(product['id'], "")
                    share_text += f"{i+1}. {product['name']} (月額: {product['monthly_fee']}円) {product_url}\n"
            
            st.text_area("共有テキスト", share_text, height=200)
        
        # 診断のやり直し
        if st.button("診断をやり直す", key="results_restart"):
            reset_session()
            go_to_questionnaire()

elif st.session_state.page == 'comparison':
    render_comparison()

else:
    st.error("ページが見つかりません")
    if st.button("ホームに戻る", key="error_home"):
        go_to_home()