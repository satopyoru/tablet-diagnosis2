import streamlit as st
from recommendation import get_recommendations

def render_questionnaire():
    st.title("📝 お子様に最適な教材を見つけるための診断")
    
    # プログレスバーの表示
    if 'question_stage' not in st.session_state:
        st.session_state.question_stage = 1
    
    progress = st.session_state.question_stage / 4
    st.progress(progress)
    st.write(f"ステップ {st.session_state.question_stage}/4")
    
    # 質問1: 学年
    if st.session_state.question_stage == 1:
        st.header("Q1: お子様の学年を教えてください")
        
        grade = st.radio(
            "学年を選択してください:",
            options=[
                "幼児（年少・年中・年長）",
                "小学校低学年（1〜3年生）",
                "小学校高学年（4〜6年生）",
                "中学生"
            ],
            index=None,
            key="grade_radio"
        )
        
        grade_mapping = {
            "幼児（年少・年中・年長）": "kindergarten",
            "小学校低学年（1〜3年生）": "lower_elementary",
            "小学校高学年（4〜6年生）": "upper_elementary",
            "中学生": "junior_high"
        }
        
        if grade:
            st.session_state.answers['grade'] = grade_mapping[grade]
            
            if st.button("次へ", type="primary"):
                st.session_state.question_stage += 1
                st.rerun()
    
    # 質問2: 学習目的
    elif st.session_state.question_stage == 2:
        st.header("Q2: どのような科目を学ばせたいですか？")
        
        subject_options = {
            "国語": "japanese",
            "算数・数学": "math",
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
            key="subjects_multiselect"
        )
        
        if selected_subjects:
            st.session_state.answers['subjects'] = [subject_options[subject] for subject in selected_subjects]
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("戻る"):
                    st.session_state.question_stage -= 1
                    st.rerun()
            with col2:
                if st.button("次へ", type="primary"):
                    st.session_state.question_stage += 1
                    st.rerun()
        else:
            if st.button("戻る"):
                st.session_state.question_stage -= 1
                st.rerun()
    
    # 質問3: 予算
    elif st.session_state.question_stage == 3:
        st.header("Q3: 月額予算を教えてください")
        
        budget = st.slider(
            "1ヶ月あたりの予算（円）:",
            min_value=1000,
            max_value=6000,
            value=st.session_state.answers.get('budget', 3000),
            step=500,
            key="budget_slider"
        )
        
        st.write(f"選択した予算: {budget}円/月")
        
        # 予算帯のコメント
        if budget < 2000:
            st.info("この予算では基本的な機能を備えた教材が選べます。特定の科目に絞った教材がおすすめです。")
        elif budget < 3500:
            st.info("この予算では一般的な総合教材や、特定分野に特化した高品質な教材が選べます。")
        else:
            st.info("この予算では最も充実した機能を持つプレミアム教材が選べます。AIによる個別最適化や豊富なコンテンツが期待できます。")
        
        st.session_state.answers['budget'] = budget
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("戻る"):
                st.session_state.question_stage -= 1
                st.rerun()
        with col2:
            if st.button("次へ", type="primary"):
                st.session_state.question_stage += 1
                st.rerun()
    
    # 質問4: 重視する機能
    elif st.session_state.question_stage == 4:
        st.header("Q4: 重視する機能を教えてください")
        
        feature_options = {
            "学習管理（進捗状況の確認、レポート機能）": "learning_management",
            "オンラインサポート（質問対応、学習相談）": "online_support",
            "教科の充実度（取り扱う科目の幅広さ）": "subject_variety",
            "問題量（練習問題の豊富さ）": "exercise_quantity",
            "双方向性（インタラクティブな学習体験）": "interactive",
            "AI学習（個別最適化された学習プラン）": "ai_learning"
        }
        
        selected_features = st.multiselect(
            "特に重視する機能を選択してください（最大3つ）:",
            options=list(feature_options.keys()),
            default=[],
            max_selections=3,
            key="features_multiselect"
        )
        
        if selected_features:
            st.session_state.answers['features'] = [feature_options[feature] for feature in selected_features]
            
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("戻る"):
                    st.session_state.question_stage -= 1
                    st.rerun()
            with col2:
                if st.button("最初からやり直す"):
                    # セッションをリセット
                    st.session_state.question_stage = 1
                    st.session_state.answers = {
                        'grade': None,
                        'subjects': [],
                        'budget': 3000,
                        'features': []
                    }
                    st.rerun()
            with col3:
                if st.button("診断結果を見る", type="primary"):
                    # 推奨事項を計算
                    recommendations = get_recommendations(st.session_state.answers)
                    st.session_state.recommendations = recommendations
                    
                    # 結果ページへ移動
                    st.session_state.page = 'results'
                    st.rerun()
        else:
            if st.button("戻る"):
                st.session_state.question_stage -= 1
                st.rerun()
    else:
        st.error("エラーが発生しました。もう一度やり直してください。")
        if st.button("最初からやり直す"):
            st.session_state.question_stage = 1
            st.session_state.answers = {
                'grade': None,
                'subjects': [],
                'budget': 3000,
                'features': []
            }
            st.rerun()
