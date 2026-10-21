from sklearn.linear_model import LinearRegression
X=[[1],[2],[3],[4],[5]]
y=[20,30,40,50,60]
model=LinearRegression()
model.fit(X,y)
predict=model.predict([[5]])
print("Hours Studied :",5)
print("Predicted Marks: ",predict[0])