import streamlit as st
import pandas as pd
import plotly.express as px
from data import tablet_data, feature_ratings, tablet_urls

def render_comparison():
    st.title("🔍 タブレット教材比較")
    
    # 比較する教材の選択
    if 'compare_ids' in st.session_state and st.session_state['compare_ids']:
        default_selection = st.session_state['compare_ids']
    else:
        default_selection = [tablet_data[0]['id'], tablet_data[1]['id']] if len(tablet_data) >= 2 else [tablet_data[0]['id']]
    
    selected_ids = st.multiselect(
        "比較したい教材を選択してください（2〜4つ推奨）",
        options=[p['id'] for p in tablet_data],
        default=default_selection,
        format_func=lambda x: next((p['name'] for p in tablet_data if p['id'] == x), x)
    )
    
    if not selected_ids:
        st.warning("比較する教材を選択してください")
        return
    
    # 選択した教材のデータを取得
    selected_products = [p for p in tablet_data if p['id'] in selected_ids]
    
    # 基本情報の比較表
    st.subheader("基本情報比較")
    
    comparison_data = []
    for product in selected_products:
        grade_range_mapping = {
            "kindergarten": "幼児",
            "lower_elementary": "小学校低学年",
            "upper_elementary": "小学校高学年",
            "junior_high": "中学生"
        }
        
        subject_mapping = {
            "japanese": "国語",
            "math": "算数/数学",
            "english": "英語",
            "science": "理科",
            "social": "社会",
            "programming": "プログラミング",
            "comprehensive": "総合学習"
        }
        
        grade_range_ja = [grade_range_mapping.get(g, g) for g in product['grade_range']]
        subjects_ja = [subject_mapping.get(s, s) for s in product['subjects']]
        
        comparison_data.append({
            "教材名": product['name'],
            "月額費用": f"{product['monthly_fee']}円",
            "初期費用": f"{product['initial_fee']}円",
            "対象学年": ", ".join(grade_range_ja),
            "対応科目": ", ".join(subjects_ja)
        })
    
    df_comparison = pd.DataFrame(comparison_data)
    st.dataframe(df_comparison, use_container_width=True)
    
    # 費用比較グラフ
    st.subheader("費用比較")
    
    # 月額費用の比較
    monthly_data = [{"教材名": p['name'], "費用（円）": p['monthly_fee'], "種類": "月額費用"} for p in selected_products]
    
    # 初期費用の比較
    initial_data = [{"教材名": p['name'], "費用（円）": p['initial_fee'], "種類": "初期費用"} for p in selected_products]
    
    # 1年間の総費用（月額×12＋初期費用）
    annual_data = [{"教材名": p['name'], "費用（円）": p['monthly_fee'] * 12 + p['initial_fee'], "種類": "1年間の総費用"} for p in selected_products]
    
    # データを結合
    cost_data = monthly_data + initial_data + annual_data
    df_cost = pd.DataFrame(cost_data)
    
    # グラフの作成
    fig = px.bar(
        df_cost, 
        x="教材名", 
        y="費用（円）", 
        color="種類",
        barmode="group",
        title="費用比較",
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # 機能比較レーダーチャート
    st.subheader("機能比較")
    
    feature_names = {
        "learning_management": "学習管理",
        "online_support": "オンラインサポート",
        "subject_variety": "教科の充実度",
        "exercise_quantity": "問題量",
        "interactive": "双方向性",
        "ai_learning": "AI学習"
    }
    
    feature_data = []
    for product in selected_products:
        product_id = product['id']
        ratings = feature_ratings.get(product_id, {})
        
        for feature, feature_ja in feature_names.items():
            rating = ratings.get(feature, 0)
            feature_data.append({
                "教材名": product['name'],
                "機能": feature_ja,
                "評価（10点満点）": rating
            })
    
    df_features = pd.DataFrame(feature_data)
    
    fig = px.line_polar(
        df_features, 
        r="評価（10点満点）", 
        theta="機能", 
        color="教材名", 
        line_close=True,
        range_r=[0,10],
        title="機能比較レーダーチャート"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # 強みと弱みの比較
    st.subheader("強みと弱みの比較")
    
    strength_tabs = st.tabs([p['name'] for p in selected_products])
    for i, tab in enumerate(strength_tabs):
        with tab:
            product = selected_products[i]
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**強み**")
                for strength in product['strengths']:
                    st.write(f"✅ {strength}")
            
            with col2:
                st.write("**弱み**")
                for weakness in product['weaknesses']:
                    st.write(f"⚠️ {weakness}")
            
            st.write("**概要**")
            st.write(product['description'])
            
            # 詳細ページへのリンク
            product_url = tablet_urls.get(product['id'], "#")
            st.write(f"[詳細ページを見る]({product_url})")
    
    # カスタム比較
    st.subheader("カスタム比較")
    
    # 比較項目の選択
    custom_options = ["月額費用", "初期費用", "1年間の総費用", "対象学年の幅広さ", "対応科目数"]
    custom_options.extend([f"機能: {f}" for f in feature_names.values()])
    
    selected_metrics = st.multiselect(
        "比較したい項目を選択してください",
        options=custom_options,
        default=["月額費用", "1年間の総費用", "機能: AI学習"]
    )
    
    if selected_metrics:
        custom_data = []
        
        for product in selected_products:
            product_data = {"教材名": product['name']}
            
            for metric in selected_metrics:
                if metric == "月額費用":
                    product_data[metric] = product['monthly_fee']
                elif metric == "初期費用":
                    product_data[metric] = product['initial_fee']
                elif metric == "1年間の総費用":
                    product_data[metric] = product['monthly_fee'] * 12 + product['initial_fee']
                elif metric == "対象学年の幅広さ":
                    product_data[metric] = len(product['grade_range'])
                elif metric == "対応科目数":
                    product_data[metric] = len(product['subjects'])
                elif metric.startswith("機能:"):
                    feature_name = metric.replace("機能: ", "")
                    feature_key = next((k for k, v in feature_names.items() if v == feature_name), None)
                    if feature_key:
                        product_data[metric] = feature_ratings.get(product['id'], {}).get(feature_key, 0)
            
            custom_data.append(product_data)
        
        df_custom = pd.DataFrame(custom_data)
        
        # 棒グラフで比較
        for metric in selected_metrics:
            if metric in df_custom.columns and metric != "教材名":
                fig = px.bar(
                    df_custom,
                    x="教材名",
                    y=metric,
                    title=f"{metric}の比較",
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
    
    # 戻るボタン
    if st.button("ホームに戻る"):
        st.session_state.page = 'home'
        st.rerun()
