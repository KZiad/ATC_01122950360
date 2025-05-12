up:
	docker-compose up --build

down:
	docker-compose down

restart:
	docker-compose down && docker-compose up --build

migrate:
	docker-compose exec web python manage.py migrate

makemigrations:
	docker-compose exec web python manage.py makemigrations

createsuperuser:
	docker-compose exec web python manage.py createsuperuser

shell:
	docker-compose exec web python manage.py shell

logs:
	docker-compose logs -f

startapp:
	docker-compose exec web python manage.py startapp $(app)

collectstatic:
	docker-compose exec web python manage.py collectstatic --noinput

sh:
	docker-compose exec web sh

clean:
	docker-compose down -v --remove-orphans
	docker system prune -f