<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

<h1>登録済みリスト</h1>

<table>
  %for row in customer_list:
    <tr>
      <td>{{row["id"]}}</td>
      <td>{{row["email"]}}</td>
      <td>{{row["age"]}}</td>
    </tr>
  %end
</table>

  </body>
</html>
