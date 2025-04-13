def f():

    massive = []
    for a in range(100, 10000):
        a_str = str(a)
        kolichestvo_a = len(a_str)

        # ��������
        if ( kolichestvo_a > 3 and a_str[1]== '0' and a_str[-2] == '0' and a % 2 != 0):
            massive.append(a)

    # ����� �����������
    if massive:
        print("��������� �����:")
        for a in massive:
            print(a)

        # ��������� ������ ����
        isp_cifra = set()
        for a in massive:
            for cifra in str(a):
                isp_cifra.add(cifra)

        # ����� ���� ��������
        print("�������������� �����:")
        cifra_propis = {
            '0': '����',
            '1': '����',
            '2': '���',
            '3': '���',
            '4': '������',
            '5': '����',
            '6': '�����',
            '7': '����',
            '8': '������',
            '9': '������',
        }

        propis = [propis[cifra] for cifra in sorted(isp_cifra)] # ���������� ��� ������������������ �������
        print(", ".join(cifra_propis))
    else:
        print("�����, �� �������.")


f()