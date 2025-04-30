import streamlit as st
from data import tablet_data, feature_ratings

def get_recommendations(answers):
    """
    ユーザーの回答に基づいて最適なタブレット教材を推薦する関数
    
    Parameters:
    answers (dict): ユーザーの回答を含む辞書
    
    Returns:
    list: 推薦されるタブレット教材のIDのリスト（スコア順）
    """
    results = []
    
    for product in tablet_data:
        score = 0
        max_score = 0
        
        # 学年の一致度をチェック
        if answers['grade'] in product['grade_range']:
            score += 20
        else:
            # 学年が合わない場合は候補から除外
            continue
        
        max_score += 20
        
        # 予算との適合性をチェック
        if product['monthly_fee'] <= answers['budget']:
            # 予算内であればフルスコア
            score += 15
        elif product['monthly_fee'] <= answers['budget'] * 1.2:
            # 予算を少し超える場合は部分スコア
            score += 5
        
        max_score += 15
        
        # 科目の一致度をチェック
        if answers['subjects']:
            subject_score = 0
            for subject in answers['subjects']:
                if subject in product['subjects']:
                    subject_score += 1
            
            # 科目スコアを正規化（最大15ポイント）
            if len(answers['subjects']) > 0:
                subject_match_percentage = subject_score / len(answers['subjects'])
                score += 15 * subject_match_percentage
            
            max_score += 15
        
        # 学習目的との適合性をチェック
        if answers.get('purpose'):
            purpose_bonus = 0
            
            if answers['purpose'] == 'catch_up':
                # 学校の授業についていくため
                if product['id'] in ['marugland', 'surara', 'tenjin', 'substa', 'schooltakt']:
                    purpose_bonus = 15
                elif product['id'] in ['challenge_touch', 'smile_zemi', 'study_suppli', 'poppy']:
                    purpose_bonus = 10
            
            elif answers['purpose'] == 'habit_formation':
                # 学習習慣を身につけるため
                if product['id'] in ['challenge_touch', 'smile_zemi', 'dekitasu', 'poppy']:
                    purpose_bonus = 15
                elif product['id'] in ['risu_kids', 'substa', 'tenjin']:
                    purpose_bonus = 10
            
            elif answers['purpose'] == 'exam_preparation':
                # 中学受験の準備のため
                if product['id'] in ['z_kai_tablet', 'toshin_online', 'risu_kids', 'study_suppli']:
                    purpose_bonus = 15
                elif product['id'] in ['smile_zemi', 'challenge_touch']:
                    purpose_bonus = 10
            
            elif answers['purpose'] == 'weakness_improvement':
                # 苦手科目を克服するため
                if product['id'] in ['risu_kids', 'tenjin', 'marugland', 'surara']:
                    purpose_bonus = 15
                elif product['id'] in ['study_suppli', 'substa']:
                    purpose_bonus = 10
            
            elif answers['purpose'] == 'advanced_learning':
                # 先取り学習・発展学習のため
                if product['id'] in ['z_kai_tablet', 'risu_kids', 'toshin_online']:
                    purpose_bonus = 15
                elif product['id'] in ['smile_zemi', 'logic_labo']:
                    purpose_bonus = 10
            
            elif answers['purpose'] == 'thinking_creativity':
                # 思考力・創造性を伸ばすため
                if product['id'] in ['logic_labo', 'wonder_box', 'groovy_lab', 'z_kai_tablet']:
                    purpose_bonus = 15
                elif product['id'] in ['thinker', 'toshin_online']:
                    purpose_bonus = 10
            
            score += purpose_bonus
            max_score += 15
        
        # 学習スタイルとの適合性をチェック
        if answers.get('learning_style'):
            style_bonus = 0
            
            if answers['learning_style'] == 'video_learning':
                # 動画授業で学ぶのが好き
                if product['id'] in ['study_suppli', 'toshin_online', 'substa']:
                    style_bonus = 15
                elif product['id'] in ['surara', 'smile_zemi', 'challenge_touch']:
                    style_bonus = 10
            
            elif answers['learning_style'] == 'gamified_learning':
                # ゲーム感覚で楽しく学びたい
                if product['id'] in ['dekitasu', 'wonder_box', 'marugland']:
                    style_bonus = 15
                elif product['id'] in ['smile_zemi', 'challenge_touch']:
                    style_bonus = 10
            
            elif answers['learning_style'] == 'self_paced':
                # 自分のペースでコツコツ取り組みたい
                if product['id'] in ['risu_kids', 'z_kai_tablet', 'schooltakt']:
                    style_bonus = 15
                elif product['id'] in ['tenjin', 'surara', 'poppy']:
                    style_bonus = 10
            
            elif answers['learning_style'] == 'experiential_learning':
                # 実験や体験を通して学びたい
                if product['id'] in ['wonder_box', 'groovy_lab']:
                    style_bonus = 15
                elif product['id'] in ['logic_labo', 'thinker']:
                    style_bonus = 10
            
            elif answers['learning_style'] == 'ai_adaptive':
                # AIが個別対応してくれる学習がいい
                if product['id'] in ['risu_kids', 'qubena', 'surara']:
                    style_bonus = 15
                elif product['id'] in ['smile_zemi', 'dekitasu', 'tenjin']:
                    style_bonus = 10
            
            elif answers['learning_style'] == 'hybrid_learning':
                # 紙とデジタルの両方を使った学習がいい
                if product['id'] in ['challenge_touch', 'z_kai_tablet', 'poppy']:
                    style_bonus = 15
                elif product['id'] in ['wonder_box', 'groovy_lab']:
                    style_bonus = 10
            
            score += style_bonus
            max_score += 15
        
        # 機能の一致度をチェック
        if answers['features']:
            feature_score = 0
            for feature in answers['features']:
                # 製品が持つ機能の評価点を加算
                feature_rating = feature_ratings.get(product['id'], {}).get(feature, 3)
                feature_score += feature_rating
            
            # 機能スコアを正規化（最大35ポイント）
            max_possible_feature_score = sum([10 for _ in answers['features']])  # 各機能の最大評価は10
            if max_possible_feature_score > 0:
                feature_match_percentage = feature_score / max_possible_feature_score
                score += 35 * feature_match_percentage
            
            max_score += 35
        
        # スコアを100点満点に正規化
        normalized_score = int((score / max_score) * 100) if max_score > 0 else 0
        
        # スコアと製品IDを結果リストに追加
        product_with_score = dict(product)
        product_with_score['match_score'] = normalized_score
        results.append((product['id'], normalized_score))
    
    # スコアの高い順にソート
    results.sort(key=lambda x: x[1], reverse=True)
    
    # スコアを更新
    for product in tablet_data:
        for product_id, score in results:
            if product['id'] == product_id:
                product['match_score'] = score
    
    # 製品IDのリストを返す
    return [product_id for product_id, _ in results]
