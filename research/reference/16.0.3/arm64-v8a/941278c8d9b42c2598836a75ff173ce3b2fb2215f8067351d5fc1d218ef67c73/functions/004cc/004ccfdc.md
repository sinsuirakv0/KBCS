# 004ccfdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "004ccfdc",
  "name": "_ZN5Botan4HMAC12key_scheduleEPKhm",
  "size": 1172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a37bef0ec351fe018f601cfb0402f4f2238bf2b5ed6aad61fed1b31f302d92e9",
  "source_text_sha256": "a37bef0ec351fe018f601cfb0402f4f2238bf2b5ed6aad61fed1b31f302d92e9"
}
~~~

## 呼び出し元

- [00c5a210](../00c5a/00c5a210.md)

## 呼び出し先

- [004b3868](../004b3/004b3868.md)
- [0054084c](../00540/0054084c.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c59130](../00c59/00c59130.md)
- [00c59700](../00c59/00c59700.md)
- [0112b058](../0112b/0112b058.md)

## 疑似コード / UTF-8 22492 bytes

~~~c

void _ZN5Botan4HMAC12key_scheduleEPKhm(long param_1,byte *param_2,ulong param_3)

{
  long lVar1;
  bool bVar2;
  ulong uVar3;
  undefined8 uVar4;
  size_t sVar5;
  byte *pbVar6;
  byte *pbVar7;
  ulong uVar8;
  byte *pbVar9;
  byte *pbVar10;
  ulong uVar11;
  long *plVar12;
  long *plVar13;
  long *plVar14;
  undefined8 uVar15;
  undefined8 uVar16;
  undefined8 uVar17;
  byte *local_70;
  byte *local_68;
  long local_60;
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  (**(code **)(**(long **)(param_1 + 0x10) + 0x38))();
  uVar3 = (**(code **)(**(long **)(param_1 + 0x10) + 0x48))();
  plVar13 = (long *)(param_1 + 0x18);
  uVar8 = *(long *)(param_1 + 0x20) - *plVar13;
  if (uVar3 < uVar8 || uVar3 - uVar8 == 0) {
    if (uVar3 < uVar8) {
      *(ulong *)(param_1 + 0x20) = *plVar13 + uVar3;
    }
  }
  else {
    FUN_0054084c(plVar13,uVar3 - uVar8);
  }
  uVar3 = (**(code **)(**(long **)(param_1 + 0x10) + 0x48))();
  plVar12 = (long *)(param_1 + 0x30);
  uVar8 = *(long *)(param_1 + 0x38) - *plVar12;
  if (uVar3 < uVar8 || uVar3 - uVar8 == 0) {
    if (uVar3 < uVar8) {
      *(ulong *)(param_1 + 0x38) = *plVar12 + uVar3;
    }
  }
  else {
    FUN_0054084c(plVar12,uVar3 - uVar8);
  }
  sVar5 = *(long *)(param_1 + 0x20) - (long)*(void **)(param_1 + 0x18);
  if (0 < (long)sVar5) {
    memset(*(void **)(param_1 + 0x18),0x36,sVar5);
  }
  sVar5 = *(long *)(param_1 + 0x38) - (long)*(void **)(param_1 + 0x30);
  if (0 < (long)sVar5) {
    memset(*(void **)(param_1 + 0x30),0x5c,sVar5);
  }
  uVar3 = (**(code **)(**(long **)(param_1 + 0x10) + 0x48))();
  if (uVar3 < param_3) {
    plVar14 = *(long **)(param_1 + 0x10);
    (**(code **)(*plVar14 + 0x18))(plVar14,param_2,param_3);
    uVar4 = (**(code **)*plVar14)(plVar14);
    FUN_004b3868(&local_70,uVar4);
    (**(code **)(*plVar14 + 0x20))(plVar14,local_70);
    pbVar10 = (byte *)*plVar13;
    pbVar6 = local_70;
    for (uVar3 = (long)local_68 - (long)local_70; 0xf < uVar3; uVar3 = uVar3 - 0x10) {
      uVar16 = *(undefined8 *)(pbVar6 + 8);
      uVar4 = *(undefined8 *)pbVar6;
      uVar17 = *(undefined8 *)(pbVar10 + 8);
      uVar15 = *(undefined8 *)pbVar10;
      *(ulong *)(pbVar10 + 8) =
           CONCAT17((byte)((ulong)uVar17 >> 0x38) ^ (byte)((ulong)uVar16 >> 0x38),
                    CONCAT16((byte)((ulong)uVar17 >> 0x30) ^ (byte)((ulong)uVar16 >> 0x30),
                             CONCAT15((byte)((ulong)uVar17 >> 0x28) ^ (byte)((ulong)uVar16 >> 0x28),
                                      CONCAT14((byte)((ulong)uVar17 >> 0x20) ^
                                               (byte)((ulong)uVar16 >> 0x20),
                                               CONCAT13((byte)((ulong)uVar17 >> 0x18) ^
                                                        (byte)((ulong)uVar16 >> 0x18),
                                                        CONCAT12((byte)((ulong)uVar17 >> 0x10) ^
                                                                 (byte)((ulong)uVar16 >> 0x10),
                                                                 CONCAT11((byte)((ulong)uVar17 >> 8)
                                                                          ^ (byte)((ulong)uVar16 >>
                                                                                  8),
                                                                          (byte)uVar17 ^
                                                                          (byte)uVar16)))))));
      *(ulong *)pbVar10 =
           CONCAT17((byte)((ulong)uVar15 >> 0x38) ^ (byte)((ulong)uVar4 >> 0x38),
                    CONCAT16((byte)((ulong)uVar15 >> 0x30) ^ (byte)((ulong)uVar4 >> 0x30),
                             CONCAT15((byte)((ulong)uVar15 >> 0x28) ^ (byte)((ulong)uVar4 >> 0x28),
                                      CONCAT14((byte)((ulong)uVar15 >> 0x20) ^
                                               (byte)((ulong)uVar4 >> 0x20),
                                               CONCAT13((byte)((ulong)uVar15 >> 0x18) ^
                                                        (byte)((ulong)uVar4 >> 0x18),
                                                        CONCAT12((byte)((ulong)uVar15 >> 0x10) ^
                                                                 (byte)((ulong)uVar4 >> 0x10),
                                                                 CONCAT11((byte)((ulong)uVar15 >> 8)
                                                                          ^ (byte)((ulong)uVar4 >> 8
                                                                                  ),
                                                                          (byte)uVar15 ^ (byte)uVar4
                                                                         )))))));
      pbVar10 = pbVar10 + 0x10;
      pbVar6 = pbVar6 + 0x10;
    }
    if (uVar3 != 0) {
      if ((7 < uVar3) && ((pbVar6 + uVar3 <= pbVar10 || (pbVar10 + uVar3 <= pbVar6)))) {
        uVar11 = uVar3 & 8;
        pbVar7 = pbVar6;
        pbVar9 = pbVar10;
        uVar8 = uVar11;
        do {
          uVar4 = *(undefined8 *)pbVar7;
          uVar16 = *(undefined8 *)pbVar9;
          uVar8 = uVar8 - 8;
          *(ulong *)pbVar9 =
               CONCAT17((byte)((ulong)uVar16 >> 0x38) ^ (byte)((ulong)uVar4 >> 0x38),
                        CONCAT16((byte)((ulong)uVar16 >> 0x30) ^ (byte)((ulong)uVar4 >> 0x30),
                                 CONCAT15((byte)((ulong)uVar16 >> 0x28) ^
                                          (byte)((ulong)uVar4 >> 0x28),
                                          CONCAT14((byte)((ulong)uVar16 >> 0x20) ^
                                                   (byte)((ulong)uVar4 >> 0x20),
                                                   CONCAT13((byte)((ulong)uVar16 >> 0x18) ^
                                                            (byte)((ulong)uVar4 >> 0x18),
                                                            CONCAT12((byte)((ulong)uVar16 >> 0x10) ^
                                                                     (byte)((ulong)uVar4 >> 0x10),
                                                                     CONCAT11((byte)((ulong)uVar16
                                                                                    >> 8) ^
                                                                              (byte)((ulong)uVar4 >>
                                                                                    8),(byte)uVar16
                                                                                       ^ (byte)uVar4
                                                                             )))))));
          pbVar7 = pbVar7 + 8;
          pbVar9 = pbVar9 + 8;
        } while (uVar8 != 0);
        bVar2 = uVar3 == uVar11;
        uVar3 = uVar3 & 7;
        pbVar6 = pbVar6 + uVar11;
        pbVar10 = pbVar10 + uVar11;
        if (bVar2) goto LAB_004cd1a4;
      }
      do {
        uVar3 = uVar3 - 1;
        *pbVar10 = *pbVar10 ^ *pbVar6;
        pbVar6 = pbVar6 + 1;
        pbVar10 = pbVar10 + 1;
      } while (uVar3 != 0);
    }
LAB_004cd1a4:
    pbVar10 = (byte *)*plVar12;
    pbVar6 = local_70;
    for (uVar3 = (long)local_68 - (long)local_70; 0xf < uVar3; uVar3 = uVar3 - 0x10) {
      uVar16 = *(undefined8 *)(pbVar6 + 8);
      uVar4 = *(undefined8 *)pbVar6;
      uVar17 = *(undefined8 *)(pbVar10 + 8);
      uVar15 = *(undefined8 *)pbVar10;
      *(ulong *)(pbVar10 + 8) =
           CONCAT17((byte)((ulong)uVar17 >> 0x38) ^ (byte)((ulong)uVar16 >> 0x38),
                    CONCAT16((byte)((ulong)uVar17 >> 0x30) ^ (byte)((ulong)uVar16 >> 0x30),
                             CONCAT15((byte)((ulong)uVar17 >> 0x28) ^ (byte)((ulong)uVar16 >> 0x28),
                                      CONCAT14((byte)((ulong)uVar17 >> 0x20) ^
                                               (byte)((ulong)uVar16 >> 0x20),
                                               CONCAT13((byte)((ulong)uVar17 >> 0x18) ^
                                                        (byte)((ulong)uVar16 >> 0x18),
                                                        CONCAT12((byte)((ulong)uVar17 >> 0x10) ^
                                                                 (byte)((ulong)uVar16 >> 0x10),
                                                                 CONCAT11((byte)((ulong)uVar17 >> 8)
                                                                          ^ (byte)((ulong)uVar16 >>
                                                                                  8),
                                                                          (byte)uVar17 ^
                                                                          (byte)uVar16)))))));
      *(ulong *)pbVar10 =
           CONCAT17((byte)((ulong)uVar15 >> 0x38) ^ (byte)((ulong)uVar4 >> 0x38),
                    CONCAT16((byte)((ulong)uVar15 >> 0x30) ^ (byte)((ulong)uVar4 >> 0x30),
                             CONCAT15((byte)((ulong)uVar15 >> 0x28) ^ (byte)((ulong)uVar4 >> 0x28),
                                      CONCAT14((byte)((ulong)uVar15 >> 0x20) ^
                                               (byte)((ulong)uVar4 >> 0x20),
                                               CONCAT13((byte)((ulong)uVar15 >> 0x18) ^
                                                        (byte)((ulong)uVar4 >> 0x18),
                                                        CONCAT12((byte)((ulong)uVar15 >> 0x10) ^
                                                                 (byte)((ulong)uVar4 >> 0x10),
                                                                 CONCAT11((byte)((ulong)uVar15 >> 8)
                                                                          ^ (byte)((ulong)uVar4 >> 8
                                                                                  ),
                                                                          (byte)uVar15 ^ (byte)uVar4
                                                                         )))))));
      pbVar10 = pbVar10 + 0x10;
      pbVar6 = pbVar6 + 0x10;
    }
    if (uVar3 != 0) {
      if ((7 < uVar3) && ((pbVar6 + uVar3 <= pbVar10 || (pbVar10 + uVar3 <= pbVar6)))) {
        uVar11 = uVar3 & 8;
        pbVar7 = pbVar6;
        pbVar9 = pbVar10;
        uVar8 = uVar11;
        do {
          uVar4 = *(undefined8 *)pbVar7;
          uVar16 = *(undefined8 *)pbVar9;
          uVar8 = uVar8 - 8;
          *(ulong *)pbVar9 =
               CONCAT17((byte)((ulong)uVar16 >> 0x38) ^ (byte)((ulong)uVar4 >> 0x38),
                        CONCAT16((byte)((ulong)uVar16 >> 0x30) ^ (byte)((ulong)uVar4 >> 0x30),
                                 CONCAT15((byte)((ulong)uVar16 >> 0x28) ^
                                          (byte)((ulong)uVar4 >> 0x28),
                                          CONCAT14((byte)((ulong)uVar16 >> 0x20) ^
                                                   (byte)((ulong)uVar4 >> 0x20),
                                                   CONCAT13((byte)((ulong)uVar16 >> 0x18) ^
                                                            (byte)((ulong)uVar4 >> 0x18),
                                                            CONCAT12((byte)((ulong)uVar16 >> 0x10) ^
                                                                     (byte)((ulong)uVar4 >> 0x10),
                                                                     CONCAT11((byte)((ulong)uVar16
                                                                                    >> 8) ^
                                                                              (byte)((ulong)uVar4 >>
                                                                                    8),(byte)uVar16
                                                                                       ^ (byte)uVar4
                                                                             )))))));
          pbVar7 = pbVar7 + 8;
          pbVar9 = pbVar9 + 8;
        } while (uVar8 != 0);
        bVar2 = uVar3 == uVar11;
        uVar3 = uVar3 & 7;
        pbVar6 = pbVar6 + uVar11;
        pbVar10 = pbVar10 + uVar11;
        if (bVar2) goto LAB_004cd21c;
      }
      do {
        uVar3 = uVar3 - 1;
        *pbVar10 = *pbVar10 ^ *pbVar6;
        pbVar6 = pbVar6 + 1;
        pbVar10 = pbVar10 + 1;
      } while (uVar3 != 0);
    }
LAB_004cd21c:
    if (local_70 != (byte *)0x0) {
      local_68 = local_70;
      (*(code *)PTR_memset_00c687d8)(local_70,0,local_60 - (long)local_70);
      free(local_70);
    }
    goto LAB_004cd348;
  }
  pbVar10 = (byte *)*plVar13;
  pbVar6 = param_2;
  for (uVar3 = param_3; 0xf < uVar3; uVar3 = uVar3 - 0x10) {
    uVar16 = *(undefined8 *)(pbVar6 + 8);
    uVar4 = *(undefined8 *)pbVar6;
    uVar17 = *(undefined8 *)(pbVar10 + 8);
    uVar15 = *(undefined8 *)pbVar10;
    *(ulong *)(pbVar10 + 8) =
         CONCAT17((byte)((ulong)uVar17 >> 0x38) ^ (byte)((ulong)uVar16 >> 0x38),
                  CONCAT16((byte)((ulong)uVar17 >> 0x30) ^ (byte)((ulong)uVar16 >> 0x30),
                           CONCAT15((byte)((ulong)uVar17 >> 0x28) ^ (byte)((ulong)uVar16 >> 0x28),
                                    CONCAT14((byte)((ulong)uVar17 >> 0x20) ^
                                             (byte)((ulong)uVar16 >> 0x20),
                                             CONCAT13((byte)((ulong)uVar17 >> 0x18) ^
                                                      (byte)((ulong)uVar16 >> 0x18),
                                                      CONCAT12((byte)((ulong)uVar17 >> 0x10) ^
                                                               (byte)((ulong)uVar16 >> 0x10),
                                                               CONCAT11((byte)((ulong)uVar17 >> 8) ^
                                                                        (byte)((ulong)uVar16 >> 8),
                                                                        (byte)uVar17 ^ (byte)uVar16)
                                                              ))))));
    *(ulong *)pbVar10 =
         CONCAT17((byte)((ulong)uVar15 >> 0x38) ^ (byte)((ulong)uVar4 >> 0x38),
                  CONCAT16((byte)((ulong)uVar15 >> 0x30) ^ (byte)((ulong)uVar4 >> 0x30),
                           CONCAT15((byte)((ulong)uVar15 >> 0x28) ^ (byte)((ulong)uVar4 >> 0x28),
                                    CONCAT14((byte)((ulong)uVar15 >> 0x20) ^
                                             (byte)((ulong)uVar4 >> 0x20),
                                             CONCAT13((byte)((ulong)uVar15 >> 0x18) ^
                                                      (byte)((ulong)uVar4 >> 0x18),
                                                      CONCAT12((byte)((ulong)uVar15 >> 0x10) ^
                                                               (byte)((ulong)uVar4 >> 0x10),
                                                               CONCAT11((byte)((ulong)uVar15 >> 8) ^
                                                                        (byte)((ulong)uVar4 >> 8),
                                                                        (byte)uVar15 ^ (byte)uVar4))
                                                     )))));
    pbVar10 = pbVar10 + 0x10;
    pbVar6 = pbVar6 + 0x10;
  }
  if (uVar3 != 0) {
    if ((7 < uVar3) && ((pbVar6 + uVar3 <= pbVar10 || (pbVar10 + uVar3 <= pbVar6)))) {
      uVar11 = uVar3 & 8;
      pbVar7 = pbVar10;
      pbVar9 = pbVar6;
      uVar8 = uVar11;
      do {
        uVar4 = *(undefined8 *)pbVar9;
        uVar16 = *(undefined8 *)pbVar7;
        uVar8 = uVar8 - 8;
        *(ulong *)pbVar7 =
             CONCAT17((byte)((ulong)uVar16 >> 0x38) ^ (byte)((ulong)uVar4 >> 0x38),
                      CONCAT16((byte)((ulong)uVar16 >> 0x30) ^ (byte)((ulong)uVar4 >> 0x30),
                               CONCAT15((byte)((ulong)uVar16 >> 0x28) ^ (byte)((ulong)uVar4 >> 0x28)
                                        ,CONCAT14((byte)((ulong)uVar16 >> 0x20) ^
                                                  (byte)((ulong)uVar4 >> 0x20),
                                                  CONCAT13((byte)((ulong)uVar16 >> 0x18) ^
                                                           (byte)((ulong)uVar4 >> 0x18),
                                                           CONCAT12((byte)((ulong)uVar16 >> 0x10) ^
                                                                    (byte)((ulong)uVar4 >> 0x10),
                                                                    CONCAT11((byte)((ulong)uVar16 >>
                                                                                   8) ^
                                                                             (byte)((ulong)uVar4 >>
                                                                                   8),(byte)uVar16 ^
                                                                                      (byte)uVar4)))
                                                 ))));
        pbVar7 = pbVar7 + 8;
        pbVar9 = pbVar9 + 8;
      } while (uVar8 != 0);
      bVar2 = uVar3 == uVar11;
      uVar3 = uVar3 & 7;
      pbVar6 = pbVar6 + uVar11;
      pbVar10 = pbVar10 + uVar11;
      if (bVar2) goto LAB_004cd2d8;
    }
    do {
      uVar3 = uVar3 - 1;
      *pbVar10 = *pbVar10 ^ *pbVar6;
      pbVar6 = pbVar6 + 1;
      pbVar10 = pbVar10 + 1;
    } while (uVar3 != 0);
  }
LAB_004cd2d8:
  pbVar10 = (byte *)*plVar12;
  for (; 0xf < param_3; param_3 = param_3 - 0x10) {
    uVar16 = *(undefined8 *)(param_2 + 8);
    uVar4 = *(undefined8 *)param_2;
    uVar17 = *(undefined8 *)(pbVar10 + 8);
    uVar15 = *(undefined8 *)pbVar10;
    *(ulong *)(pbVar10 + 8) =
         CONCAT17((byte)((ulong)uVar17 >> 0x38) ^ (byte)((ulong)uVar16 >> 0x38),
                  CONCAT16((byte)((ulong)uVar17 >> 0x30) ^ (byte)((ulong)uVar16 >> 0x30),
                           CONCAT15((byte)((ulong)uVar17 >> 0x28) ^ (byte)((ulong)uVar16 >> 0x28),
                                    CONCAT14((byte)((ulong)uVar17 >> 0x20) ^
                                             (byte)((ulong)uVar16 >> 0x20),
                                             CONCAT13((byte)((ulong)uVar17 >> 0x18) ^
                                                      (byte)((ulong)uVar16 >> 0x18),
                                                      CONCAT12((byte)((ulong)uVar17 >> 0x10) ^
                                                               (byte)((ulong)uVar16 >> 0x10),
                                                               CONCAT11((byte)((ulong)uVar17 >> 8) ^
                                                                        (byte)((ulong)uVar16 >> 8),
                                                                        (byte)uVar17 ^ (byte)uVar16)
                                                              ))))));
    *(ulong *)pbVar10 =
         CONCAT17((byte)((ulong)uVar15 >> 0x38) ^ (byte)((ulong)uVar4 >> 0x38),
                  CONCAT16((byte)((ulong)uVar15 >> 0x30) ^ (byte)((ulong)uVar4 >> 0x30),
                           CONCAT15((byte)((ulong)uVar15 >> 0x28) ^ (byte)((ulong)uVar4 >> 0x28),
                                    CONCAT14((byte)((ulong)uVar15 >> 0x20) ^
                                             (byte)((ulong)uVar4 >> 0x20),
                                             CONCAT13((byte)((ulong)uVar15 >> 0x18) ^
                                                      (byte)((ulong)uVar4 >> 0x18),
                                                      CONCAT12((byte)((ulong)uVar15 >> 0x10) ^
                                                               (byte)((ulong)uVar4 >> 0x10),
                                                               CONCAT11((byte)((ulong)uVar15 >> 8) ^
                                                                        (byte)((ulong)uVar4 >> 8),
                                                                        (byte)uVar15 ^ (byte)uVar4))
                                                     )))));
    pbVar10 = pbVar10 + 0x10;
    param_2 = param_2 + 0x10;
  }
  if (param_3 != 0) {
    if ((7 < param_3) && ((param_2 + param_3 <= pbVar10 || (pbVar10 + param_3 <= param_2)))) {
      uVar8 = param_3 & 8;
      pbVar6 = pbVar10;
      uVar3 = uVar8;
      pbVar7 = param_2;
      do {
        uVar4 = *(undefined8 *)pbVar7;
        uVar16 = *(undefined8 *)pbVar6;
        uVar3 = uVar3 - 8;
        *(ulong *)pbVar6 =
             CONCAT17((byte)((ulong)uVar16 >> 0x38) ^ (byte)((ulong)uVar4 >> 0x38),
                      CONCAT16((byte)((ulong)uVar16 >> 0x30) ^ (byte)((ulong)uVar4 >> 0x30),
                               CONCAT15((byte)((ulong)uVar16 >> 0x28) ^ (byte)((ulong)uVar4 >> 0x28)
                                        ,CONCAT14((byte)((ulong)uVar16 >> 0x20) ^
                                                  (byte)((ulong)uVar4 >> 0x20),
                                                  CONCAT13((byte)((ulong)uVar16 >> 0x18) ^
                                                           (byte)((ulong)uVar4 >> 0x18),
                                                           CONCAT12((byte)((ulong)uVar16 >> 0x10) ^
                                                                    (byte)((ulong)uVar4 >> 0x10),
                                                                    CONCAT11((byte)((ulong)uVar16 >>
                                                                                   8) ^
                                                                             (byte)((ulong)uVar4 >>
                                                                                   8),(byte)uVar16 ^
                                                                                      (byte)uVar4)))
                                                 ))));
        pbVar6 = pbVar6 + 8;
        pbVar7 = pbVar7 + 8;
      } while (uVar3 != 0);
      bVar2 = param_3 == uVar8;
      param_3 = param_3 & 7;
      param_2 = param_2 + uVar8;
      pbVar10 = pbVar10 + uVar8;
      if (bVar2) goto LAB_004cd348;
    }
    do {
      param_3 = param_3 - 1;
      *pbVar10 = *pbVar10 ^ *param_2;
      param_2 = param_2 + 1;
      pbVar10 = pbVar10 + 1;
    } while (param_3 != 0);
  }
LAB_004cd348:
  (**(code **)(**(long **)(param_1 + 0x10) + 0x18))
            (*(long **)(param_1 + 0x10),*(long *)(param_1 + 0x18),
             *(long *)(param_1 + 0x20) - *(long *)(param_1 + 0x18));
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
