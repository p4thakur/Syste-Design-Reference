# #Script to make sql update statement from csv
# import pandas

# df = pandas.read_excel('dueAmount.xls')

# list1=df.columns.ravel();
# #print(df['account_number'].tolist())
# due_date= df['due_date'];
#accountnumber=df['account_number'];
# print(len(accountnumber))
# for i in range(len(accountnumber)):
#   a='update accounts set due_date=\''+str(due_date[i])+ '\' where account_number=\''+str(accountnumber[i])+'\';'
#   f = open("demo.txt", "a")
#   f.write(a)
#   f.write("\n")
#Script to make sql update statement from csv
import pandas

df = pandas.read_excel('emi_repayment_billing_data.xls')

list1=df.columns.ravel();
#print(df['account_number'].tolist())
# priciple= df['Principal'];
# interest= df['interest'];
# emi_txn_id= df['emi_txn_id']
# # duedate=df['duedate']
# installment= df['amount'];
# principal= df['principal'];
# interest= df['interest'];
#accountnumber=df['loan_account_number'];
# lmsAccountNumber=df['loan_account_number'];
# accountnumber=df['postpaid_account_number'];
orderid=df['merchant_order_id'];
amount= df['amount'];
repayid=df['id'];

print(len(repayid))
for i in range(len(repayid)):
  a1='update emi_repayment set order=\''+str(orderid[i])+ '\' where id=\''+str(repayid[i])+'\';'
  #update repayment set metadata = json_set(metadata, '$.emiAmount', 635.00), updated_at = updated_at, record_updated_at = now() where merchant_order_id= '26185931';
  a2='update repayment set metadata = json_set(metadata, \'$.emiAmount\','+str(amount[i])+'\'), updated_at = updated_at, record_updated_at = now() where merchant_order_id=\''+str(orderid[i])+'\';'
  # a1='update accounts set emi_on_hold=\''+str(amount[i])+ '\' where account_number=\''+str(accountnumber[i])+'\';'
  # a1='update accounts set available_credit_limit=available_credit_limit-\''+str(interest[i])+ '\' where account_number=\''+str(accountnumber[i])+'\';'
  # a2='update accounts set due_amount=due_amount+\''+str(installment[i])+ '\' where account_number=\''+str(accountnumber[i])+'\';'
  # a3='update accounts set bill_amount=bill_amount+\''+str(installment[i])+ '\' where account_number=\''+str(accountnumber[i])+'\';'
  # a4='update bills set total_amt=total_amt+\''+str(installment[i])+ '\' where month=9 and account_number=\''+str(accountnumber[i])+'\';'
  # a5='INSERT INTO `emi_applied_transactions` (`postpaid_account_number`,`lms_account_number`,`lms_txn_id`,`amount`,`principal`,`interest`,`remarks`,`status`,`txn_date`) '\
  # ' VALUES (\''+str(accountnumber[i])+'\',\''+str(lmsAccountNumber[i])+'\',"Manual_edit","PRAT"\''+str(installment[i])+'\',"Thak"\''+str(principal[i])+'\',"UR"\''+str(interest[i])+'\',"Due for Installment",0,"2021-09-01 00:00:00");'
  
  # a5='INSERT INTO `emi_applied_transactions` (`lms_account_number`,`lms_txn_id`,`amount`,`principal`,`interest`,`remarks`,`status`,`txn_date`) '\
  # ' VALUES (\''+str(accountnumber[i])+'\',\''+str(lmsAccountNumber[i])+'\',"Manual_edit","PRAT"\''+str(installment[i])+'\',"Thak"\''+str(principal[i])+'\',"UR"\''+str(interest[i])+'\',"Due for Installment",0,'+str(duedate[i])+'\'");'
  
  # # a='INSERT INTO manual_update_audit (loan_account_number,`column`, `table`, update_type, old_value, new_value) '\
  #    'SELECT account_number, "due_date","accounts", "UPDATE", '\
  #    'JSON_OBJECT( "due_date",due_date ),JSON_OBJECT( "due_date",\''+str(due_date1[i])+'\') FROM accounts '\
  #     'where account_number=\''+str(accountnumber[i])+'\';'
  # a3='INSERT INTO statement (reference_id,`type`,`amount`,`status`,`account_number`,`metadata`) '\
  # 'VALUES (\''+str(emi_txn_id[i])+'\',12,\''+str(installment[i])+'\',0,\''+str(accountnumber[i])+'\','\
  # '\'{\\\"title\\\":\\\"Installment Due \\\",\\\"extRefId\\\":null,\\\"updatedBalance\\\":null,\\\"updatedMonthlyLimit\\\":null,\\\"receivedViaSI\\\":null,\\\"merchantDisplayName\\\":null,\\\"merchantType\\\":null,\\\"fulfilmentId\\\":null,\\\"orderItemId\\\":null,\\\"imageUrl\\\":null,\\\"originalTransactionId\\\":null,\\\"source\\\":\\\"past Emi Due manual edit \\\"}\');'
  # # # # f = open("Emi_on_hold.txt", "a")
  # f.write(a)
  # f.write("\n")
  f1 = open("emi_repayment_october.txt", "a")
  f1.write(a1)
  f1.write("\n")
  f2 = open("repayment_octoner.txt", "a")
  f2.write(a2)
  f2.write("\n")
  # f3 = open("missing_emi_statement.txt", "a")
  # f3.write(a3)
  # f3.write("\n")
  # f4 = open("emi_due_bills_total_amount.txt", "a")
  # f4.write(a4)
  # f4.write("\n")
  # a='update bills set total_amt=total_amt+\''+str(installment[i])+ '\',emi_amt=emi_amt+\''+str(installment[i])+ '\' where month=9 and account_number=\''+str(accountnumber[i])+'\';'
  # a1='update bills set due_amt=greatest(total_amt, due_amt) where month=9 and account_number=\''+str(accountnumber[i])+'\';'
  # a2='update accounts set due_amount=due_amount + +\''+str(installment[i])+ '\' where account_number=\''+str(accountnumber[i])+'\';'

  # #update bills set total_amt=total_amt+100, emi_amt=emi_amt+100 where account_number='' and month=9;
  # f1 = open("emi_missing_Emi_transaction", "a")
  # f1.write(a5)
  # f1.write("\n")   
  # f2 = open("emi_missing_avaiable_limit", "a")
  # f2.write(a1)
  # f2.write("\n")   
  # f2 = open("emi_update_due", "a")
  # f2.write(a1)
  # f2.write("\n") 
  # f3 = open("emi_update_account", "a")
  # f3.write(a2)
  # f3.write("\n") 

