import streamlit as st
from recommendation import get_recommendations

def render_questionnaire():
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
                recommendations = get_recommendations(st.session_state.answers)
                st.session_state.recommendations = recommendations
                st.session_state.page = 'results'