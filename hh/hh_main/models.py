from django.db import models


class TgmUser(models.Model):
    #id = models.IntegerField(primary_key=True)
    tgm_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=100)

    def get_user(self, tgm_id, username):
        TgmUser.objects.get_or_create(
            tgm_id=tgm_id,
            username=username,
             )


class UserSettings(models.Model):
    expected_experience: models.IntegerField()
    salary = models.IntegerField()
    user = models.OneToOneField(TgmUser, on_delete=models.CASCADE, primary_key=True)


class KeyWords(models.Model):
    word = models.CharField(max_length=1_000)
    user = models.ManyToManyField(TgmUser, related_name='tgmuser')


class UserStopWords(models.Model):
    word = models.CharField(max_length=10_000)
    user = models.ManyToManyField(TgmUser)


class UserGoodWords(models.Model):
    word = models.CharField(max_length=10_000)
    user = models.ManyToManyField(TgmUser)


class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    user = models.ManyToManyField(TgmUser)


class Company(models.Model):
    word = models.CharField(max_length=100)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)


class UserVacancyStatus(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='uv_vacancy')
    user = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='uv_user')


class UserVacancyRating(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='s_vacancy')
    user = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='s_user')
    first_auto_score = models.IntegerField()
    second_auto_score = models.IntegerField()
    user_score = models.IntegerField()

class VacancyStatus(models.Model):
    name = models.CharField(max_length=20)
    status = models.ForeignKey(UserVacancyStatus, on_delete=models.SET_NULL, null=True, related_name='status')

