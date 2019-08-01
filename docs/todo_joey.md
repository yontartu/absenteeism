# to do
- EDA visualizations (scatter plots, qq plots for normality, residuals plots)
- interaction terms?
- time series 
	- look at MA and AR parts
	- ACF/PACF
- logistic regression 
	 - choose target (hit target)
	 

andy's ideas:
- gb month and day of week, take average value of absenteeism - DONE
- look for mo-over-mo trends - DONE
 pass into seasonal decompose function, help see trend over time (jan-dec), and seasonality for day-to-day - DONE
- logreg, do one, interpret it, share results
- change threshold and see if that helps
- use .predict_proba() ? 


# later
- group by id, to see distribution, look at total number of employees in the dataset
- deal with 40/80/120 target variable values - DONE (just dropped them)


# done
- dont set nulls to zero - DONE
- first: train test split - DONE
- don't scale your target - DONE
- break X into dummy and continuous - DONE
- fit/transform train data - DONE 
- transform test data with same scaler (which is already fitted with training data) - DONE
- use LassoCV - DONE

- recursive feature elimination - DONE
	- do we want to use X or X_train to pick features? - DONE
- try lasso - DONE
	- first standardize (standard scalar from sklearn.preprocessing) - DONE
- report results of model of choice w/ statsmodels (more information) - DONE
- try k-folds crossvalidation - DONE
- AIC/BIC - DONE
