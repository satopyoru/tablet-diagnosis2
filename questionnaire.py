import streamlit as st
from recommendation import get_recommendations

def render_questionnaire():
    st.title("📝 お子様に最適な教材を見つけるための診断")
    
    # プログレスバーの表示
    if 'question_stage' not in st.session_state:
        st.session_state.question_stage = 1
    
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
            "思考力・論理的思考": "thinking",
            "アート・創造性": "art",
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
            key="purpose_radio"
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
                if st.button("戻る"):
                    st.session_state.question_stage -= 1
                    st.rerun()
            with col2:
                if st.button("次へ", type="primary"):
                    st.session_state.question_stage += 1
                    st.rerun()
    
    # 質問4: 学習スタイル
    elif st.session_state.question_stage == 4:
        st.header("Q4: お子様にぴったりの学習スタイルは？")
        
        style = st.radio(
            "お子様の性格や好みに合うものを選んでください:",
            options=[
                "動画授業で学ぶのが好き",
                "ゲーム感覚で楽しく学びたい",
                "自分のペースでコツコツ取り組みたい",
                "実験や体験を通して学びたい",
                "AIが個別対応してくれる学習がいい",
                "紙とデジタルの両方を使った学習がいい"
            ],
            index=None,
            key="style_radio"
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
                if st.button("戻る"):
                    st.session_state.question_stage -= 1
                    st.rerun()
            with col2:
                if st.button("次へ", type="primary"):
                    st.session_state.question_stage += 1
                    st.rerun()
    
    # 質問5: 予算
    elif st.session_state.question_stage == 5:
        st.header("Q5: 月額予算を教えてください")
        
        budget = st.slider(
            "1ヶ月あたりの予算（円）:",
            min_value=980,
            max_value=9000,
            value=st.session_state.answers.get('budget', 3000),
            step=500,
            key="budget_slider"
        )
        
        st.write(f"選択した予算: {budget}円/月")
        
        # 予算帯のコメント
        if budget < 2000:
            st.info("この予算では、サブスタやまるぐランドなど、基本的な機能を備えたリーズナブルな教材が選べます。")
        elif budget < 3500:
            st.info("この予算では、チャレンジタッチやスマイルゼミなど、一般的な総合教材や特定分野に特化した教材が選べます。")
        elif budget < 5000:
            st.info("この予算では、Z会やすららなど、より高度な内容や個別最適化機能を持つ教材が選べます。")
        else:
            st.info("この予算では、東進オンライン学校など、難関受験対策や専門的な指導が受けられる高品質な教材が選べます。")
        
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
    
    # 質問6: 重視する機能
    elif st.session_state.question_stage == 6:
        st.header("Q6: 重視する機能を教えてください")
        
        feature_options = {
            "学習管理機能（進捗状況の確認、レポート）": "learning_management",
            "オンラインサポート（質問対応、学習相談）": "online_support",
            "教科の充実度（取り扱う科目の幅広さ）": "subject_variety",
            "問題量（練習問題の豊富さ）": "exercise_quantity",
            "双方向性（インタラクティブな学習体験）": "interactive",
            "AI学習（個別最適化された学習プラン）": "ai_learning",
            "思考力・論理的思考力の養成": "thinking_skills",
            "コストパフォーマンスの良さ": "cost_effective",
            "動画授業の質と量": "video_lessons",
            "テスト対策の充実度": "test_preparation",
            "発展的な学習内容": "advanced_learning",
            "特別支援・学習につまずきのある子向け機能": "special_needs_support",
            "創造性を育む内容": "creativity",
            "STEM教育（理数系+技術）": "stem_education",
            "プロジェクト型学習": "project_based"
        }
        
        selected_features = st.multiselect(
            "特に重視する機能を選択してください（最大5つ）:",
            options=list(feature_options.keys()),
            default=[],
            max_selections=5,
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
                        'features': [],
                        'purpose': None,
                        'learning_style': None
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
                'features': [],
                'purpose': None,
                'learning_style': None
            }
            st.rerun()
