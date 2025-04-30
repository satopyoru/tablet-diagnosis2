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
            score += 25
        else:
            # 学年が合わない場合は候補から除外
            continue
        
        max_score += 25
        
        # 予算との適合性をチェック
        if product['monthly_fee'] <= answers['budget']:
            # 予算内であればフルスコア
            score += 20
        elif product['monthly_fee'] <= answers['budget'] * 1.2:
            # 予算を少し超える場合は部分スコア
            score += 10
        
        max_score += 20
        
        # 科目の一致度をチェック
        if answers['subjects']:
            subject_score = 0
            for subject in answers['subjects']:
                if subject in product['subjects']:
                    subject_score += 1
            
            # 科目スコアを正規化（最大25ポイント）
            if len(answers['subjects']) > 0:
                subject_match_percentage = subject_score / len(answers['subjects'])
                score += 25 * subject_match_percentage
            
            max_score += 25
        
        # 機能の一致度をチェック
        if answers['features']:
            feature_score = 0
            for feature in answers['features']:
                if feature in product['features']:
                    # 製品が持つ機能の評価点を加算
                    feature_rating = feature_ratings.get(product['id'], {}).get(feature, 5)
                    feature_score += feature_rating
            
            # 機能スコアを正規化（最大30ポイント）
            max_possible_feature_score = sum([10 for _ in answers['features']])  # 各機能の最大評価は10
            if max_possible_feature_score > 0:
                feature_match_percentage = feature_score / max_possible_feature_score
                score += 30 * feature_match_percentage
            
            max_score += 30
        
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
