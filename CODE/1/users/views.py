from django.shortcuts import render, HttpResponse
from .forms import UserRegistrationForm
from django.contrib import messages
from .models import UserRegistrationModel
from users.utility.process_ml import Algorithms
import numpy as np
algo = Algorithms()


# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'register.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(
                loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(
                    request, 'Your Account has not been activated by Admin.')
                return render(request, 'user.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'user.html', {})


def UserHome(request):
    return render(request, 'users/UserHome.html', {})


def logout(request):
    return render(request, 'user.html', {})
# RF


def random_forest(request):
    prec, recall, f1 = algo.calc_random_forest_Classifier()
    return render(request, "users/RF.html", {'prec': prec, 'recall': recall, 'f1': f1})

# NB


def navie_bayes(request):
    prec, recall, f1 = algo.calc_naive_bayes_Classifier()
    print(f1)
    return render(request, "users/navie_bayes.html", {'prec': prec, 'recall': recall, 'f1': f1})
# SVM


def svm(request):
    prec, recall, f1 = algo.calc_support_vector_machine_Classifier()

    return render(request, "users/svm.html", {'prec': prec, 'recall': recall, 'f1': f1})


def logistic_regression(request):
    prec, recall, f1 = algo.calc_logistic_Regression()

    return render(request, "users/LR.html", {'prec': prec, 'recall': recall, 'f1': f1})


def DT(request):
    prec, recall, f1 = algo.calc_DT_Classifier()

    return render(request, "users/DT.html", {'prec': prec, 'recall': recall, 'f1': f1})


def KNN(request):
    prec, recall, f1 = algo.calc_KNN_Classifier()

    return render(request, "users/KNN.html", {'prec': prec, 'recall': recall, 'f1': f1})


def predict(request):
    if request.method == 'POST':
        No_of_reviews = int(request.POST.get('No_of_reviews'))
        No_of_ingredients = int(request.POST.get('No_of_ ingredients'))
        No_of_servings = int(request.POST.get('No_of_servings'))
        No_of_instructions = int(request.POST.get('No_of_instructions'))
        test_set = [No_of_reviews, No_of_ingredients,
                    No_of_servings, No_of_instructions]

        result = algo.test_userInput(test_set)
        if result[0] == 1:
            msg = 'Good'
        else:
            msg = "Bad"

        return render(request, "users/predict.html", {'result': msg})
    else:
        return render(request, "users/predict.html")
