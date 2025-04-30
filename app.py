import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import plotly.express as px

from questionnaire import render_questionnaire
from comparison import render_comparison
from recommendation import get_recommendations
from data import tablet_data

# アプリの設定
st.set_page_config(
    page_title="子供のタブレット教材診断ツール",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# セッションステートの初期化
if 'page' not in st.session_state:
    st.session_state.page = 'home'

if 'answers' not in st.session_state:
    st.session_state.answers = {
        'grade': None,
        'subjects': [],
        'budget': 3000,
        'features': []
    }

if 'recommendations' not in st.session_state:
    st.session_state.recommendations = []

def reset_session():
    st.session_state.page = 'home'
    st.session_state.answers = {
        'grade': None,
        'subjects': [],
        'budget': 3000,
        'features': []
    }
    st.session_state.recommendations = []
    st.rerun()

# サイドバー
with st.sidebar:
    st.title("メニュー")
    
    if st.button("ホーム"):
        st.session_state.page = 'home'
        st.rerun()
    
    if st.button("診断スタート"):
        st.session_state.page = 'questionnaire'
        st.rerun()
    
    if st.button("教材比較"):
        st.session_state.page = 'comparison'
        st.rerun()
    
    if st.button("診断結果"):
        if not st.session_state.recommendations:
            st.error("まずは診断を完了させてください")
        else:
            st.session_state.page = 'results'
            st.rerun()
    
    st.divider()
    if st.button("リセット"):
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
        if st.button("診断を始める", use_container_width=True, type="primary"):
            st.session_state.page = 'questionnaire'
            st.rerun()
    with col2:
        if st.button("教材を比較する", use_container_width=True):
            st.session_state.page = 'comparison'
            st.rerun()

elif st.session_state.page == 'questionnaire':
    render_questionnaire()

elif st.session_state.page == 'results':
    st.title("🎯 診断結果")
    
    if not st.session_state.recommendations:
        st.error("診断結果がありません。診断をやり直してください。")
        if st.button("診断に戻る"):
            st.session_state.page = 'questionnaire'
            st.rerun()
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
                    'comprehensive': '総合学習'
                }
                subjects = [subject_mapping.get(s, s) for s in st.session_state.answers['subjects']]
                st.write(f"**学習目的**: {', '.join(subjects)}")
                
                feature_mapping = {
                    'learning_management': '学習管理',
                    'online_support': 'オンラインサポート',
                    'subject_variety': '教科の充実度',
                    'exercise_quantity': '問題量',
                    'interactive': '双方向性',
                    'ai_learning': 'AI学習'
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
                st.subheader(f"{i+1}. {product['name']}")
                st.write(f"**月額**: {product['monthly_fee']}円")
                st.write(f"**初期費用**: {product['initial_fee']}円")
                match_score = product.get('match_score', 0)
                st.progress(match_score/100)
                st.write(f"マッチ度: {match_score}%")
            
            with col2:
                st.write(f"**特徴**: {product['description']}")
                
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
            options=[p['id'] for p in tablet_data if p['id'] in st.session_state.recommendations],
            default=st.session_state.recommendations[:2] if len(st.session_state.recommendations) >= 2 else st.session_state.recommendations,
            format_func=lambda x: next((p['name'] for p in tablet_data if p['id'] == x), x)
        )
        
        if st.button("選択した教材を比較する"):
            st.session_state['compare_ids'] = compare_ids
            st.session_state.page = 'comparison'
            st.rerun()
        
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
                    share_text += f"{i+1}. {product['name']} (月額: {product['monthly_fee']}円)\n"
            
            st.text_area("共有テキスト", share_text, height=200)
        
        # 診断のやり直し
        if st.button("診断をやり直す"):
            reset_session()
            st.session_state.page = 'questionnaire'
            st.rerun()

elif st.session_state.page == 'comparison':
    render_comparison()

else:
    st.error("ページが見つかりません")
    if st.button("ホームに戻る"):
        st.session_state.page = 'home'
        st.rerun()
