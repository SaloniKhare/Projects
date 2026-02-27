from hpp import X,Y
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2, random_state=0)

column_trans = make_column_transformer((OneHotEncoder(sparse_output=False),['location']),remainder='passthrough')
scalar=StandardScaler()

'''#Linear Regression Model
lr=LinearRegression()
pipe=make_pipeline(column_trans,scalar,lr)
pipe.fit(X_train,Y_train)
Y_pred_lr=pipe.predict(X_test)
print(r2_score(Y_test,Y_pred_lr))

#Lasso Model
lasso=Lasso()
pipe=make_pipeline(column_trans,scalar,lasso)
pipe.fit(X_train,Y_train)
Y_pred_lasso=pipe.predict(X_test)
print(r2_score(Y_test,Y_pred_lasso))'''

#Ridge Model
ridge=Ridge()
pipe=make_pipeline(column_trans,scalar,ridge)
pipe.fit(X_train,Y_train)
Y_pred_ridge=pipe.predict(X_test)
r2_score(Y_test,Y_pred_ridge)

pickle.dump(pipe,open('RidgeModel.pkl','wb'))