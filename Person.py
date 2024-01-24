class person:
    def __init__(self,LastName,Name,Phone,Description):
        self.LastName = LastName
        self.Name = Name
        self.Phone=Phone
        self.Description = Description
    def ToString(self):
        print(f"Имя: {self.Name}, Фамилия: {self.LastName}, Телефон: {self.Phone}, Описание: {self.Description}")