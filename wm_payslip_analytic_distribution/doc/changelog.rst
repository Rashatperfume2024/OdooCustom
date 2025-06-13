v1.0.0
======
  - Add analytic account field to the header of the customer Invoices /Credit Notes / Vendor Bills /Refunds.
  - Once a user added a new line, this field will be passed as a default value to the new line analytic account field.
  - Header analytic account will be read only if the invoice/Credit Notes/Bill/Refunds is not in draft state.
  - Header analytic account will be visible only for users who has "Analytic Accounting" right.
  - You can apply header analytic account to all lines.