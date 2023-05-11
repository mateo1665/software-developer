dagen = ('maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag')
welke_dag = input(f'welke dag kies je {dagen}')
dag_van_de_week = 0

while dag_van_de_week < 8:
    if dagen[dag_van_de_week] == welke_dag:
        break
    print(dagen[dag_van_de_week])
    print(dag_van_de_week)
    dag_van_de_week += 1
