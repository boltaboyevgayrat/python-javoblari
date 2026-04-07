def minimize_waiting_time(tasks):
    # 1. Topshiriqlarni bajarilish vaqti bo'yicha o'sish tartibida saralaymiz
    # tasks ro'yxati (id, duration) ko'rinishida bo'lishi mumkin
    tasks.sort(key=lambda x: x[1])

    waiting_times = []
    current_waiting_time = 0
    total_waiting_time = 0

    print("Optimal bajarilish tartibi:")
    for i, (task_id, duration) in enumerate(tasks):
        waiting_times.append(current_waiting_time)
        print(f"{i+1}-navbat: Topshiriq {task_id} (Davomiyligi: {duration}, Kutish: {current_waiting_time})")
        
        total_waiting_time += current_waiting_time
        current_waiting_time += duration

    avg_waiting_time = total_waiting_time / len(tasks)
    
    return total_waiting_time, avg_waiting_time

# Sinov ma'lumotlari: (ID, Davomiylik)
job_list = [("A", 10), ("B", 3), ("C", 5), ("D", 2)]

total, avg = minimize_waiting_time(job_list)

print("-" * 30)
print(f"Jami kutish vaqti: {total}")
print(f"O'rtacha kutish vaqti: {avg:.2f}")