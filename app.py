from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    cv_data = {
        "nama": "Ken Ratu",
        "tempat_lahir": "Duri",
        "tanggal_lahir": "28 Juni 2005",
        "domisili": "Pekanbaru",
        "email": "ken24trse@mahasiswa.pcr.ac.id",
        "whatsapp": "085213744859",
        "linkedin": "ken-ratu-sembiring",
        "tentang": "Saya mahasiswa yang fokus pada elektronika, pemrograman, dan pengembangan sistem. Saya belajar proyek mikrokontroler, sistem digital, dan pengembangan web.",
        "pendidikan": {
            "kampus": "Politeknik Caltex Riau",
            "prodi": "Teknologi Rekayasa Sistem Elektronika",
            "masuk": "2024"
        },
        "keahlian": ["Arduino", "HTML", "CSS", "Python dasar", "Analisis rangkaian listrik", "Microsoft Office"],
        "soft_skills": ["Problem solving", "Teamwork", "Disiplin", "Manajemen waktu"],
        "pengalaman": [
            {
                "posisi": "Pengurus HIMA bidang kewirausahaan",
                "deskripsi": ["Mengelola kegiatan kewirausahaan dan program kerja organisasi."]
            },
            {
                "posisi": "Bendahara inti PCR Pelalawan",
                "deskripsi": ["Mengelola keuangan, mencatat transaksi, menyusun laporan kegiatan dan memastikan penggunaan dana sesuai program kerja."]
            },
            {
                "posisi": "Technical Facilitator & Pengajar",
                "deskripsi": ["Mendampingi pelatihan IoT dan mengajar teknologi dasar di pesantren."]
            },
            {
                "posisi": "MC E Sport Riau & Pemateri",
                "deskripsi": ["Memimpin acara e-sport dan memberikan pelatihan teknologi."]
            }
        ],
        "aktivitas": ["Panitia Sore Akrab PCR Pelalawan 2024", "Panitia Musyawarah Besar PCR Pelalawan 2024", "Peserta Diklat Organisasi 2025", "Promosi Kampus PCR GTS 2025", "UKM Roboarm Aktif", "Panitia Musyawarah Besar HIMIKA 2025", "Pelatihan IoT Pesantren Darussalam", "Panitia Elka Festival 2025", "Panitia PCR E Sport Competition 2025"],
        "prestasi": ["Juara 1 dan Juara 2 lomba tingkat nasional bidang Matematika, Biologi, dan Kimia", "Top 100 Puisi Nasional"],
        "proyek": ["Line Follower Robot Berbasis Mikrokontroler", "Jam Digital Berbasis Seven Segment"],
        "hobi": ["Menulis puisi", "Membaca", "Mendengarkan musik", "Memasak"]
    }
    return render_template('index.html', data=cv_data)

if __name__ == '__main__':
    app.run(debug=True)