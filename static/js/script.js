function testText() {
	document.getElementById('text').value = 'Офис и шоу-рум в Красноярске работает с 14.00 до 17.00 по адресу г.Красноряск ул.Парижской Коммуны,14 оф.14.\n' +
		'Юридический адрес: 129344, г. Москва, ул. Искры, Иванов Иван Иванович дом 31, корпус 1, пом. II комната 7А.\n' +
		'г. Пятигорск, ул. Февральская, д. 54\n' +
		'Дмитровское шоссе, д.157, стр.9\n' +
		'603070, г. Нижний Новгород, ул. Акимова 22 «А»\n' +
		'Адрес: | г. Санкт-Петербург, ул. Шамшева, д. 8 (ДК им.В.А.Шелгунова)\n' +
		'Факт. и юр. адрес: 426052, г. Ижевск, ул. Лесозаводская 23/110\n' +
		'Адрес: Россия г. Санкт-Петербург ул. Чехова 14 оф23\n' +
		'129085, 1000 рублей 50 копеек Петров Павел Дмитриевич Москва, ул.Годовикова д.9  (Бизнес-центр "Калибр").\n' +
		'Почтовый адрес: Россия, 693010 г. Южно-Сахалинск, Комсомольская, 154, оф. 600\n' +
		'ул. Менжинского, 4г ст. А\n' +
		'344010, РФ, 1 доллар г. Ростов-на-Дону, ул. Красноармейская д.208, офис 302.\n' +
		'Юридический адрес 308000, Белгородская обл., г.Белгород, ул.Н.Островского, д.5\n' +
		'Юридический, физический и фактический адрес: 350072, г. Краснодар, ул. Московская, 5.\n' +
		'10 июня 1991 года  Российская Федерация, Тверская область, Кимрский район, пгт.  Белый Городок, улица Заводская дом 11\n' +
		'Свердловская обл., г. Екатеринбург, Барвинка 21';
}

function reSend() {
	document.getElementById('result').classList.add("d-none");
	document.getElementById('form').classList.remove("d-none");
	document.getElementById('text').value = '';
	document.getElementById("t_fios").innerHTML = '';
	document.getElementById("t_dates").innerHTML = '';
	document.getElementById("t_address").innerHTML = '';
	document.getElementById("t_cashes").innerHTML = '';
	document.getElementById("original_text").innerHTML = '';
}

function sendText() {
	var text = document.getElementById("text").value;
	var xhr = new XMLHttpRequest();
	var body = 'text=' + encodeURIComponent(text);
	document.getElementById('form').classList.add("d-none");
	document.getElementById('loader').classList.remove("d-none");

	xhr.open("POST", '/service', true);
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			document.getElementById('loader').classList.add("d-none");
			document.getElementById('result').classList.remove("d-none");
			var response = JSON.parse(this.responseText);
			document.getElementById("original_text").innerHTML = response.original_text;
			var t_fios = document.getElementById("t_fios");
			var i;
			for (i = 0; i < response.names.length; i++) {
				var tr = document.createElement('tr');
				var td_first = document.createElement('td');
				var td_middle = document.createElement('td');
				var td_last = document.createElement('td');
				td_first.innerHTML = response.names[i].first;
				td_middle.innerHTML = response.names[i].middle;
				td_last.innerHTML = response.names[i].last;
				tr.appendChild(td_first);
				tr.appendChild(td_middle);
				tr.appendChild(td_last);
				t_fios.appendChild(tr);
			}
			var t_dates = document.getElementById("t_dates");
			for (i = 0; i < response.dates.length; i++) {
				var tr = document.createElement('tr');
				var td_day = document.createElement('td');
				var td_month = document.createElement('td');
				var td_year = document.createElement('td');
				td_day.innerHTML = response.dates[i].day;
				td_month.innerHTML = response.dates[i].month;
				td_year.innerHTML = response.dates[i].year;
				tr.appendChild(td_day);
				tr.appendChild(td_month);
				tr.appendChild(td_year);
				t_dates.appendChild(tr);
			}

			var t_address = document.getElementById("t_address");
			for (i = 0; i < response.addresses.length; i++) {
				var tr = document.createElement('tr');
				var td_address = document.createElement('td');
				td_address.innerHTML = response.addresses[i];
				tr.appendChild(td_address);
				t_address.appendChild(tr);
			}

			var t_cashes = document.getElementById("t_cashes");
			for (i = 0; i < response.cashes.length; i++) {
				var tr = document.createElement('tr');
				var td_integer = document.createElement('td');
				var td_coins = document.createElement('td');
				var td_fraction = document.createElement('td');
				var td_multiplier = document.createElement('td');
				var td_currency = document.createElement('td');
				td_integer.innerHTML = response.cashes[i].integer;
				td_coins.innerHTML = response.cashes[i].coins;
				td_fraction.innerHTML = response.cashes[i].fraction;
				td_multiplier.innerHTML = response.cashes[i].multiplier;
				td_currency.innerHTML = response.cashes[i].currency;
				tr.appendChild(td_integer);
				tr.appendChild(td_coins);
				tr.appendChild(td_fraction);
				tr.appendChild(td_multiplier);
				tr.appendChild(td_currency);
				t_cashes.appendChild(tr);
			}
		}
	};
	xhr.send(body);
}


function get_resource() {
	var xhr = new XMLHttpRequest();
	xhr.open('GET', 'http://213.108.129.190/xml/get-temp-data', true);
	xhr.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			console.log(JSON.parse(this.responseText));
		}
	};
	xhr.send();
}