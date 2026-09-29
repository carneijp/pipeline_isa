import sklearn 
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

def main():
    path = "/workspaces/imparare-surface-materdei-neo/ScriptsLibrary/pipeline/T6/utilities"
    model = joblib.load(f"{path}/modelo1_stephani2.joblib")

    feature_importances = model.feature_importances_
    features = model.feature_names_in_

    del model

    importance_df = pd.DataFrame({
        'Feature': features,
        'Importance': feature_importances
    }).sort_values(by='Importance', ascending=False)

    # Plot Feature Importances
    plt.figure(figsize=(8, 16))
    plt.barh(importance_df['Feature'], importance_df['Importance'])
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.title('Feature Importances')
    plt.gca().invert_yaxis()  # To show the most important feature at the top
    plt.show()

if __name__ == "__main__":
    main()