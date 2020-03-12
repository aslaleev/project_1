<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.11"></script>

    <select v-model="selected">
        <option disabled value="">Выберите один из вариантов</option>
        <option>А</option>
        <option>Б</option>
        <option>В</option>
    </select>
    <script>
        new Vue({
        el: '...',
        data: {
        selected: ''
  }
        })
    </script>

</body>
</html>