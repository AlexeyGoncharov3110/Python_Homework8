import view
import model

def start_prog():
    expression= view.data_start()
    exp_pars=model.expression_pars(expression)
    sum_mult=model.mult(exp_pars)
    sum_div=model.div(sum_mult)
    sum_sub=model.sub(sum_div)
    sum_expression=model.addit(sum_sub)
    view.result(sum_expression)
    

    
    