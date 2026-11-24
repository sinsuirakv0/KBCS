# 004ccfdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `004cccbc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cccbc.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0002.md#compare-5828aa812ead223c940c77d81252794c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "a37bef0ec351fe018f601cfb0402f4f2238bf2b5ed6aad61fed1b31f302d92e9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004ccfdc",
        "004cd46b"
      ],
      [
        "004cd494",
        "004cd497"
      ]
    ],
    "bytes_sha256": "81217a1d81451a8df7aecbc955fb79c8fb680d24fd3e2d82c37752fe36351176",
    "instruction_count": 293,
    "instruction_bytes": 1172,
    "body_bytes": 1172,
    "indirect": 9,
    "unresolved": 8
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004ccfdc"></a> `004ccfdc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-004ccfe0"></a> `004ccfe0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004ccfe4"></a> `004ccfe4` | `f9 1b 00 f9` | str x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004ccfe8"></a> `004ccfe8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004ccfec"></a> `004ccfec` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004ccff0"></a> `004ccff0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004ccff4"></a> `004ccff4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004ccff8"></a> `004ccff8` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004ccffc"></a> `004ccffc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004cd000"></a> `004cd000` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-004cd004"></a> `004cd004` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-004cd008"></a> `004cd008` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-004cd00c"></a> `004cd00c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cd010"></a> `004cd010` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004cd014"></a> `004cd014` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004cd018"></a> `004cd018` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-004cd01c"></a> `004cd01c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cd020"></a> `004cd020` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004cd024"></a> `004cd024` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004cd028"></a> `004cd028` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-004cd02c"></a> `004cd02c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cd030"></a> `004cd030` | `f7 03 13 aa` | mov x23,x19 | `FALL_THROUGH`
<a id="insn-004cd034"></a> `004cd034` | `e8 a6 c1 a9` | ldp x8,x9,[x23, #0x18]! | `FALL_THROUGH`
<a id="insn-004cd038"></a> `004cd038` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004cd03c"></a> `004cd03c` | `01 00 09 eb` | subs x1,x0,x9 | `FALL_THROUGH`
<a id="insn-004cd040"></a> `004cd040` | `89 00 00 54` | b.ls 0x004cd050 | `CONDITIONAL_JUMP`
<a id="insn-004cd044"></a> `004cd044` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-004cd048"></a> `004cd048` | `01 ce 01 94` | bl 0x0054084c | `UNCONDITIONAL_CALL`
<a id="insn-004cd04c"></a> `004cd04c` | `04 00 00 14` | b 0x004cd05c | `UNCONDITIONAL_JUMP`
<a id="insn-004cd050"></a> `004cd050` | `62 00 00 54` | b.cs 0x004cd05c | `CONDITIONAL_JUMP`
<a id="insn-004cd054"></a> `004cd054` | `08 01 00 8b` | add x8,x8,x0 | `FALL_THROUGH`
<a id="insn-004cd058"></a> `004cd058` | `68 12 00 f9` | str x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-004cd05c"></a> `004cd05c` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004cd060"></a> `004cd060` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004cd064"></a> `004cd064` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-004cd068"></a> `004cd068` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cd06c"></a> `004cd06c` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-004cd070"></a> `004cd070` | `88 26 c3 a9` | ldp x8,x9,[x20, #0x30]! | `FALL_THROUGH`
<a id="insn-004cd074"></a> `004cd074` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004cd078"></a> `004cd078` | `01 00 09 eb` | subs x1,x0,x9 | `FALL_THROUGH`
<a id="insn-004cd07c"></a> `004cd07c` | `89 00 00 54` | b.ls 0x004cd08c | `CONDITIONAL_JUMP`
<a id="insn-004cd080"></a> `004cd080` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004cd084"></a> `004cd084` | `f2 cd 01 94` | bl 0x0054084c | `UNCONDITIONAL_CALL`
<a id="insn-004cd088"></a> `004cd088` | `04 00 00 14` | b 0x004cd098 | `UNCONDITIONAL_JUMP`
<a id="insn-004cd08c"></a> `004cd08c` | `62 00 00 54` | b.cs 0x004cd098 | `CONDITIONAL_JUMP`
<a id="insn-004cd090"></a> `004cd090` | `08 01 00 8b` | add x8,x8,x0 | `FALL_THROUGH`
<a id="insn-004cd094"></a> `004cd094` | `68 1e 00 f9` | str x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-004cd098"></a> `004cd098` | `60 a2 41 a9` | ldp x0,x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-004cd09c"></a> `004cd09c` | `02 01 00 cb` | sub x2,x8,x0 | `FALL_THROUGH`
<a id="insn-004cd0a0"></a> `004cd0a0` | `5f 04 00 f1` | cmp x2,#0x1 | `FALL_THROUGH`
<a id="insn-004cd0a4"></a> `004cd0a4` | `6b 00 00 54` | b.lt 0x004cd0b0 | `CONDITIONAL_JUMP`
<a id="insn-004cd0a8"></a> `004cd0a8` | `c1 06 80 52` | mov w1,#0x36 | `FALL_THROUGH`
<a id="insn-004cd0ac"></a> `004cd0ac` | `21 30 1e 94` | bl 0x00c59130 | `UNCONDITIONAL_CALL`
<a id="insn-004cd0b0"></a> `004cd0b0` | `60 22 43 a9` | ldp x0,x8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-004cd0b4"></a> `004cd0b4` | `02 01 00 cb` | sub x2,x8,x0 | `FALL_THROUGH`
<a id="insn-004cd0b8"></a> `004cd0b8` | `5f 04 00 f1` | cmp x2,#0x1 | `FALL_THROUGH`
<a id="insn-004cd0bc"></a> `004cd0bc` | `6b 00 00 54` | b.lt 0x004cd0c8 | `CONDITIONAL_JUMP`
<a id="insn-004cd0c0"></a> `004cd0c0` | `81 0b 80 52` | mov w1,#0x5c | `FALL_THROUGH`
<a id="insn-004cd0c4"></a> `004cd0c4` | `1b 30 1e 94` | bl 0x00c59130 | `UNCONDITIONAL_CALL`
<a id="insn-004cd0c8"></a> `004cd0c8` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004cd0cc"></a> `004cd0cc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004cd0d0"></a> `004cd0d0` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-004cd0d4"></a> `004cd0d4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cd0d8"></a> `004cd0d8` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-004cd0dc"></a> `004cd0dc` | `a2 0b 00 54` | b.cs 0x004cd250 | `CONDITIONAL_JUMP`
<a id="insn-004cd0e0"></a> `004cd0e0` | `78 0a 40 f9` | ldr x24,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004cd0e4"></a> `004cd0e4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-004cd0e8"></a> `004cd0e8` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-004cd0ec"></a> `004cd0ec` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-004cd0f0"></a> `004cd0f0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-004cd0f4"></a> `004cd0f4` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-004cd0f8"></a> `004cd0f8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cd0fc"></a> `004cd0fc` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-004cd100"></a> `004cd100` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-004cd104"></a> `004cd104` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-004cd108"></a> `004cd108` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cd10c"></a> `004cd10c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-004cd110"></a> `004cd110` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004cd114"></a> `004cd114` | `d5 99 ff 97` | bl 0x004b3868 | `UNCONDITIONAL_CALL`
<a id="insn-004cd118"></a> `004cd118` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-004cd11c"></a> `004cd11c` | `e1 03 40 f9` | ldr x1,[sp] | `FALL_THROUGH`
<a id="insn-004cd120"></a> `004cd120` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-004cd124"></a> `004cd124` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-004cd128"></a> `004cd128` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cd12c"></a> `004cd12c` | `e8 27 40 a9` | ldp x8,x9,[sp] | `FALL_THROUGH`
<a id="insn-004cd130"></a> `004cd130` | `2a 01 08 cb` | sub x10,x9,x8 | `FALL_THROUGH`
<a id="insn-004cd134"></a> `004cd134` | `e9 02 40 f9` | ldr x9,[x23] | `FALL_THROUGH`
<a id="insn-004cd138"></a> `004cd138` | `5f 41 00 f1` | cmp x10,#0x10 | `FALL_THROUGH`
<a id="insn-004cd13c"></a> `004cd13c` | `03 01 00 54` | b.cc 0x004cd15c | `CONDITIONAL_JUMP`
<a id="insn-004cd140"></a> `004cd140` | `00 05 c1 3c` | ldr q0,[x8], #0x10 | `FALL_THROUGH`
<a id="insn-004cd144"></a> `004cd144` | `21 01 c0 3d` | ldr q1,[x9] | `FALL_THROUGH`
<a id="insn-004cd148"></a> `004cd148` | `4a 41 00 d1` | sub x10,x10,#0x10 | `FALL_THROUGH`
<a id="insn-004cd14c"></a> `004cd14c` | `20 1c 20 6e` | eor v0.16B,v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-004cd150"></a> `004cd150` | `5f 3d 00 f1` | cmp x10,#0xf | `FALL_THROUGH`
<a id="insn-004cd154"></a> `004cd154` | `20 05 81 3c` | str q0,[x9], #0x10 | `FALL_THROUGH`
<a id="insn-004cd158"></a> `004cd158` | `48 ff ff 54` | b.hi 0x004cd140 | `CONDITIONAL_JUMP`
<a id="insn-004cd15c"></a> `004cd15c` | `4a 02 00 b4` | cbz x10,0x004cd1a4 | `CONDITIONAL_JUMP`
<a id="insn-004cd160"></a> `004cd160` | `5f 21 00 f1` | cmp x10,#0x8 | `FALL_THROUGH`
<a id="insn-004cd164"></a> `004cd164` | `e3 00 00 54` | b.cc 0x004cd180 | `CONDITIONAL_JUMP`
<a id="insn-004cd168"></a> `004cd168` | `0b 01 0a 8b` | add x11,x8,x10 | `FALL_THROUGH`
<a id="insn-004cd16c"></a> `004cd16c` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-004cd170"></a> `004cd170` | `62 14 00 54` | b.cs 0x004cd3fc | `CONDITIONAL_JUMP`
<a id="insn-004cd174"></a> `004cd174` | `2b 01 0a 8b` | add x11,x9,x10 | `FALL_THROUGH`
<a id="insn-004cd178"></a> `004cd178` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-004cd17c"></a> `004cd17c` | `02 14 00 54` | b.cs 0x004cd3fc | `CONDITIONAL_JUMP`
<a id="insn-004cd180"></a> `004cd180` | `eb 03 0a aa` | mov x11,x10 | `FALL_THROUGH`
<a id="insn-004cd184"></a> `004cd184` | `ec 03 08 aa` | mov x12,x8 | `FALL_THROUGH`
<a id="insn-004cd188"></a> `004cd188` | `ed 03 09 aa` | mov x13,x9 | `FALL_THROUGH`
<a id="insn-004cd18c"></a> `004cd18c` | `88 15 40 38` | ldrb w8,[x12], #0x1 | `FALL_THROUGH`
<a id="insn-004cd190"></a> `004cd190` | `a9 01 40 39` | ldrb w9,[x13] | `FALL_THROUGH`
<a id="insn-004cd194"></a> `004cd194` | `6b 05 00 f1` | subs x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-004cd198"></a> `004cd198` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-004cd19c"></a> `004cd19c` | `a8 15 00 38` | strb w8,[x13], #0x1 | `FALL_THROUGH`
<a id="insn-004cd1a0"></a> `004cd1a0` | `61 ff ff 54` | b.ne 0x004cd18c | `CONDITIONAL_JUMP`
<a id="insn-004cd1a4"></a> `004cd1a4` | `e8 27 40 a9` | ldp x8,x9,[sp] | `FALL_THROUGH`
<a id="insn-004cd1a8"></a> `004cd1a8` | `2a 01 08 cb` | sub x10,x9,x8 | `FALL_THROUGH`
<a id="insn-004cd1ac"></a> `004cd1ac` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-004cd1b0"></a> `004cd1b0` | `5f 41 00 f1` | cmp x10,#0x10 | `FALL_THROUGH`
<a id="insn-004cd1b4"></a> `004cd1b4` | `03 01 00 54` | b.cc 0x004cd1d4 | `CONDITIONAL_JUMP`
<a id="insn-004cd1b8"></a> `004cd1b8` | `00 05 c1 3c` | ldr q0,[x8], #0x10 | `FALL_THROUGH`
<a id="insn-004cd1bc"></a> `004cd1bc` | `21 01 c0 3d` | ldr q1,[x9] | `FALL_THROUGH`
<a id="insn-004cd1c0"></a> `004cd1c0` | `4a 41 00 d1` | sub x10,x10,#0x10 | `FALL_THROUGH`
<a id="insn-004cd1c4"></a> `004cd1c4` | `20 1c 20 6e` | eor v0.16B,v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-004cd1c8"></a> `004cd1c8` | `5f 3d 00 f1` | cmp x10,#0xf | `FALL_THROUGH`
<a id="insn-004cd1cc"></a> `004cd1cc` | `20 05 81 3c` | str q0,[x9], #0x10 | `FALL_THROUGH`
<a id="insn-004cd1d0"></a> `004cd1d0` | `48 ff ff 54` | b.hi 0x004cd1b8 | `CONDITIONAL_JUMP`
<a id="insn-004cd1d4"></a> `004cd1d4` | `4a 02 00 b4` | cbz x10,0x004cd21c | `CONDITIONAL_JUMP`
<a id="insn-004cd1d8"></a> `004cd1d8` | `5f 21 00 f1` | cmp x10,#0x8 | `FALL_THROUGH`
<a id="insn-004cd1dc"></a> `004cd1dc` | `e3 00 00 54` | b.cc 0x004cd1f8 | `CONDITIONAL_JUMP`
<a id="insn-004cd1e0"></a> `004cd1e0` | `0b 01 0a 8b` | add x11,x8,x10 | `FALL_THROUGH`
<a id="insn-004cd1e4"></a> `004cd1e4` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-004cd1e8"></a> `004cd1e8` | `62 12 00 54` | b.cs 0x004cd434 | `CONDITIONAL_JUMP`
<a id="insn-004cd1ec"></a> `004cd1ec` | `2b 01 0a 8b` | add x11,x9,x10 | `FALL_THROUGH`
<a id="insn-004cd1f0"></a> `004cd1f0` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-004cd1f4"></a> `004cd1f4` | `02 12 00 54` | b.cs 0x004cd434 | `CONDITIONAL_JUMP`
<a id="insn-004cd1f8"></a> `004cd1f8` | `eb 03 0a aa` | mov x11,x10 | `FALL_THROUGH`
<a id="insn-004cd1fc"></a> `004cd1fc` | `ec 03 08 aa` | mov x12,x8 | `FALL_THROUGH`
<a id="insn-004cd200"></a> `004cd200` | `ed 03 09 aa` | mov x13,x9 | `FALL_THROUGH`
<a id="insn-004cd204"></a> `004cd204` | `88 15 40 38` | ldrb w8,[x12], #0x1 | `FALL_THROUGH`
<a id="insn-004cd208"></a> `004cd208` | `a9 01 40 39` | ldrb w9,[x13] | `FALL_THROUGH`
<a id="insn-004cd20c"></a> `004cd20c` | `6b 05 00 f1` | subs x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-004cd210"></a> `004cd210` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-004cd214"></a> `004cd214` | `a8 15 00 38` | strb w8,[x13], #0x1 | `FALL_THROUGH`
<a id="insn-004cd218"></a> `004cd218` | `61 ff ff 54` | b.ne 0x004cd204 | `CONDITIONAL_JUMP`
<a id="insn-004cd21c"></a> `004cd21c` | `f4 03 40 f9` | ldr x20,[sp] | `FALL_THROUGH`
<a id="insn-004cd220"></a> `004cd220` | `54 09 00 b4` | cbz x20,0x004cd348 | `CONDITIONAL_JUMP`
<a id="insn-004cd224"></a> `004cd224` | `f4 07 00 f9` | str x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004cd228"></a> `004cd228` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004cd22c"></a> `004cd22c` | `c9 3c 00 f0` | adrp x9,0xc68000 | `FALL_THROUGH`
<a id="insn-004cd230"></a> `004cd230` | `29 ed 43 f9` | ldr x9,[x9, #0x7d8] | `FALL_THROUGH`
<a id="insn-004cd234"></a> `004cd234` | `02 01 14 cb` | sub x2,x8,x20 | `FALL_THROUGH`
<a id="insn-004cd238"></a> `004cd238` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004cd23c"></a> `004cd23c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004cd240"></a> `004cd240` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004cd244"></a> `004cd244` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004cd248"></a> `004cd248` | `2e 31 1e 94` | bl 0x00c59700 | `UNCONDITIONAL_CALL`
<a id="insn-004cd24c"></a> `004cd24c` | `3f 00 00 14` | b 0x004cd348 | `UNCONDITIONAL_JUMP`
<a id="insn-004cd250"></a> `004cd250` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-004cd254"></a> `004cd254` | `bf 42 00 f1` | cmp x21,#0x10 | `FALL_THROUGH`
<a id="insn-004cd258"></a> `004cd258` | `83 01 00 54` | b.cc 0x004cd288 | `CONDITIONAL_JUMP`
<a id="insn-004cd25c"></a> `004cd25c` | `ea 03 15 aa` | mov x10,x21 | `FALL_THROUGH`
<a id="insn-004cd260"></a> `004cd260` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-004cd264"></a> `004cd264` | `20 05 c1 3c` | ldr q0,[x9], #0x10 | `FALL_THROUGH`
<a id="insn-004cd268"></a> `004cd268` | `01 01 c0 3d` | ldr q1,[x8] | `FALL_THROUGH`
<a id="insn-004cd26c"></a> `004cd26c` | `4a 41 00 d1` | sub x10,x10,#0x10 | `FALL_THROUGH`
<a id="insn-004cd270"></a> `004cd270` | `20 1c 20 6e` | eor v0.16B,v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-004cd274"></a> `004cd274` | `5f 3d 00 f1` | cmp x10,#0xf | `FALL_THROUGH`
<a id="insn-004cd278"></a> `004cd278` | `00 05 81 3c` | str q0,[x8], #0x10 | `FALL_THROUGH`
<a id="insn-004cd27c"></a> `004cd27c` | `48 ff ff 54` | b.hi 0x004cd264 | `CONDITIONAL_JUMP`
<a id="insn-004cd280"></a> `004cd280` | `aa 00 00 b5` | cbnz x10,0x004cd294 | `CONDITIONAL_JUMP`
<a id="insn-004cd284"></a> `004cd284` | `15 00 00 14` | b 0x004cd2d8 | `UNCONDITIONAL_JUMP`
<a id="insn-004cd288"></a> `004cd288` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-004cd28c"></a> `004cd28c` | `ea 03 15 aa` | mov x10,x21 | `FALL_THROUGH`
<a id="insn-004cd290"></a> `004cd290` | `4a 02 00 b4` | cbz x10,0x004cd2d8 | `CONDITIONAL_JUMP`
<a id="insn-004cd294"></a> `004cd294` | `5f 21 00 f1` | cmp x10,#0x8 | `FALL_THROUGH`
<a id="insn-004cd298"></a> `004cd298` | `e3 00 00 54` | b.cc 0x004cd2b4 | `CONDITIONAL_JUMP`
<a id="insn-004cd29c"></a> `004cd29c` | `2b 01 0a 8b` | add x11,x9,x10 | `FALL_THROUGH`
<a id="insn-004cd2a0"></a> `004cd2a0` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-004cd2a4"></a> `004cd2a4` | `42 07 00 54` | b.cs 0x004cd38c | `CONDITIONAL_JUMP`
<a id="insn-004cd2a8"></a> `004cd2a8` | `0b 01 0a 8b` | add x11,x8,x10 | `FALL_THROUGH`
<a id="insn-004cd2ac"></a> `004cd2ac` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-004cd2b0"></a> `004cd2b0` | `e2 06 00 54` | b.cs 0x004cd38c | `CONDITIONAL_JUMP`
<a id="insn-004cd2b4"></a> `004cd2b4` | `eb 03 0a aa` | mov x11,x10 | `FALL_THROUGH`
<a id="insn-004cd2b8"></a> `004cd2b8` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-004cd2bc"></a> `004cd2bc` | `ed 03 08 aa` | mov x13,x8 | `FALL_THROUGH`
<a id="insn-004cd2c0"></a> `004cd2c0` | `88 15 40 38` | ldrb w8,[x12], #0x1 | `FALL_THROUGH`
<a id="insn-004cd2c4"></a> `004cd2c4` | `a9 01 40 39` | ldrb w9,[x13] | `FALL_THROUGH`
<a id="insn-004cd2c8"></a> `004cd2c8` | `6b 05 00 f1` | subs x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-004cd2cc"></a> `004cd2cc` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-004cd2d0"></a> `004cd2d0` | `a8 15 00 38` | strb w8,[x13], #0x1 | `FALL_THROUGH`
<a id="insn-004cd2d4"></a> `004cd2d4` | `61 ff ff 54` | b.ne 0x004cd2c0 | `CONDITIONAL_JUMP`
<a id="insn-004cd2d8"></a> `004cd2d8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-004cd2dc"></a> `004cd2dc` | `bf 42 00 f1` | cmp x21,#0x10 | `FALL_THROUGH`
<a id="insn-004cd2e0"></a> `004cd2e0` | `03 01 00 54` | b.cc 0x004cd300 | `CONDITIONAL_JUMP`
<a id="insn-004cd2e4"></a> `004cd2e4` | `c0 06 c1 3c` | ldr q0,[x22], #0x10 | `FALL_THROUGH`
<a id="insn-004cd2e8"></a> `004cd2e8` | `01 01 c0 3d` | ldr q1,[x8] | `FALL_THROUGH`
<a id="insn-004cd2ec"></a> `004cd2ec` | `b5 42 00 d1` | sub x21,x21,#0x10 | `FALL_THROUGH`
<a id="insn-004cd2f0"></a> `004cd2f0` | `20 1c 20 6e` | eor v0.16B,v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-004cd2f4"></a> `004cd2f4` | `bf 3e 00 f1` | cmp x21,#0xf | `FALL_THROUGH`
<a id="insn-004cd2f8"></a> `004cd2f8` | `00 05 81 3c` | str q0,[x8], #0x10 | `FALL_THROUGH`
<a id="insn-004cd2fc"></a> `004cd2fc` | `48 ff ff 54` | b.hi 0x004cd2e4 | `CONDITIONAL_JUMP`
<a id="insn-004cd300"></a> `004cd300` | `55 02 00 b4` | cbz x21,0x004cd348 | `CONDITIONAL_JUMP`
<a id="insn-004cd304"></a> `004cd304` | `bf 22 00 f1` | cmp x21,#0x8 | `FALL_THROUGH`
<a id="insn-004cd308"></a> `004cd308` | `e3 00 00 54` | b.cc 0x004cd324 | `CONDITIONAL_JUMP`
<a id="insn-004cd30c"></a> `004cd30c` | `c9 02 15 8b` | add x9,x22,x21 | `FALL_THROUGH`
<a id="insn-004cd310"></a> `004cd310` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004cd314"></a> `004cd314` | `82 05 00 54` | b.cs 0x004cd3c4 | `CONDITIONAL_JUMP`
<a id="insn-004cd318"></a> `004cd318` | `09 01 15 8b` | add x9,x8,x21 | `FALL_THROUGH`
<a id="insn-004cd31c"></a> `004cd31c` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-004cd320"></a> `004cd320` | `22 05 00 54` | b.cs 0x004cd3c4 | `CONDITIONAL_JUMP`
<a id="insn-004cd324"></a> `004cd324` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-004cd328"></a> `004cd328` | `ea 03 16 aa` | mov x10,x22 | `FALL_THROUGH`
<a id="insn-004cd32c"></a> `004cd32c` | `eb 03 08 aa` | mov x11,x8 | `FALL_THROUGH`
<a id="insn-004cd330"></a> `004cd330` | `48 15 40 38` | ldrb w8,[x10], #0x1 | `FALL_THROUGH`
<a id="insn-004cd334"></a> `004cd334` | `6c 01 40 39` | ldrb w12,[x11] | `FALL_THROUGH`
<a id="insn-004cd338"></a> `004cd338` | `29 05 00 f1` | subs x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004cd33c"></a> `004cd33c` | `88 01 08 4a` | eor w8,w12,w8 | `FALL_THROUGH`
<a id="insn-004cd340"></a> `004cd340` | `68 15 00 38` | strb w8,[x11], #0x1 | `FALL_THROUGH`
<a id="insn-004cd344"></a> `004cd344` | `61 ff ff 54` | b.ne 0x004cd330 | `CONDITIONAL_JUMP`
<a id="insn-004cd348"></a> `004cd348` | `60 06 41 a9` | ldp x0,x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004cd34c"></a> `004cd34c` | `69 12 40 f9` | ldr x9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-004cd350"></a> `004cd350` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004cd354"></a> `004cd354` | `22 01 01 cb` | sub x2,x9,x1 | `FALL_THROUGH`
<a id="insn-004cd358"></a> `004cd358` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-004cd35c"></a> `004cd35c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cd360"></a> `004cd360` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-004cd364"></a> `004cd364` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cd368"></a> `004cd368` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004cd36c"></a> `004cd36c` | `41 09 00 54` | b.ne 0x004cd494 | `CONDITIONAL_JUMP`
<a id="insn-004cd370"></a> `004cd370` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004cd374"></a> `004cd374` | `f9 1b 40 f9` | ldr x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004cd378"></a> `004cd378` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004cd37c"></a> `004cd37c` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004cd380"></a> `004cd380` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004cd384"></a> `004cd384` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-004cd388"></a> `004cd388` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004cd38c"></a> `004cd38c` | `4e 01 7d 92` | and x14,x10,#0x8 | `FALL_THROUGH`
<a id="insn-004cd390"></a> `004cd390` | `4b 09 40 92` | and x11,x10,#0x7 | `FALL_THROUGH`
<a id="insn-004cd394"></a> `004cd394` | `2c 01 0e 8b` | add x12,x9,x14 | `FALL_THROUGH`
<a id="insn-004cd398"></a> `004cd398` | `0d 01 0e 8b` | add x13,x8,x14 | `FALL_THROUGH`
<a id="insn-004cd39c"></a> `004cd39c` | `ef 03 0e aa` | mov x15,x14 | `FALL_THROUGH`
<a id="insn-004cd3a0"></a> `004cd3a0` | `20 85 40 fc` | ldr d0,[x9], #0x8 | `FALL_THROUGH`
<a id="insn-004cd3a4"></a> `004cd3a4` | `01 01 40 fd` | ldr d1,[x8] | `FALL_THROUGH`
<a id="insn-004cd3a8"></a> `004cd3a8` | `ef 21 00 f1` | subs x15,x15,#0x8 | `FALL_THROUGH`
<a id="insn-004cd3ac"></a> `004cd3ac` | `20 1c 20 2e` | eor v0.8B,v1.8B,v0.8B | `FALL_THROUGH`
<a id="insn-004cd3b0"></a> `004cd3b0` | `00 85 00 fc` | str d0,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-004cd3b4"></a> `004cd3b4` | `61 ff ff 54` | b.ne 0x004cd3a0 | `CONDITIONAL_JUMP`
<a id="insn-004cd3b8"></a> `004cd3b8` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-004cd3bc"></a> `004cd3bc` | `21 f8 ff 54` | b.ne 0x004cd2c0 | `CONDITIONAL_JUMP`
<a id="insn-004cd3c0"></a> `004cd3c0` | `c6 ff ff 17` | b 0x004cd2d8 | `UNCONDITIONAL_JUMP`
<a id="insn-004cd3c4"></a> `004cd3c4` | `ac 02 7d 92` | and x12,x21,#0x8 | `FALL_THROUGH`
<a id="insn-004cd3c8"></a> `004cd3c8` | `a9 0a 40 92` | and x9,x21,#0x7 | `FALL_THROUGH`
<a id="insn-004cd3cc"></a> `004cd3cc` | `ca 02 0c 8b` | add x10,x22,x12 | `FALL_THROUGH`
<a id="insn-004cd3d0"></a> `004cd3d0` | `0b 01 0c 8b` | add x11,x8,x12 | `FALL_THROUGH`
<a id="insn-004cd3d4"></a> `004cd3d4` | `ed 03 0c aa` | mov x13,x12 | `FALL_THROUGH`
<a id="insn-004cd3d8"></a> `004cd3d8` | `c0 86 40 fc` | ldr d0,[x22], #0x8 | `FALL_THROUGH`
<a id="insn-004cd3dc"></a> `004cd3dc` | `01 01 40 fd` | ldr d1,[x8] | `FALL_THROUGH`
<a id="insn-004cd3e0"></a> `004cd3e0` | `ad 21 00 f1` | subs x13,x13,#0x8 | `FALL_THROUGH`
<a id="insn-004cd3e4"></a> `004cd3e4` | `20 1c 20 2e` | eor v0.8B,v1.8B,v0.8B | `FALL_THROUGH`
<a id="insn-004cd3e8"></a> `004cd3e8` | `00 85 00 fc` | str d0,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-004cd3ec"></a> `004cd3ec` | `61 ff ff 54` | b.ne 0x004cd3d8 | `CONDITIONAL_JUMP`
<a id="insn-004cd3f0"></a> `004cd3f0` | `bf 02 0c eb` | cmp x21,x12 | `FALL_THROUGH`
<a id="insn-004cd3f4"></a> `004cd3f4` | `e1 f9 ff 54` | b.ne 0x004cd330 | `CONDITIONAL_JUMP`
<a id="insn-004cd3f8"></a> `004cd3f8` | `d4 ff ff 17` | b 0x004cd348 | `UNCONDITIONAL_JUMP`
<a id="insn-004cd3fc"></a> `004cd3fc` | `4e 01 7d 92` | and x14,x10,#0x8 | `FALL_THROUGH`
<a id="insn-004cd400"></a> `004cd400` | `4b 09 40 92` | and x11,x10,#0x7 | `FALL_THROUGH`
<a id="insn-004cd404"></a> `004cd404` | `0c 01 0e 8b` | add x12,x8,x14 | `FALL_THROUGH`
<a id="insn-004cd408"></a> `004cd408` | `2d 01 0e 8b` | add x13,x9,x14 | `FALL_THROUGH`
<a id="insn-004cd40c"></a> `004cd40c` | `ef 03 0e aa` | mov x15,x14 | `FALL_THROUGH`
<a id="insn-004cd410"></a> `004cd410` | `00 85 40 fc` | ldr d0,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-004cd414"></a> `004cd414` | `21 01 40 fd` | ldr d1,[x9] | `FALL_THROUGH`
<a id="insn-004cd418"></a> `004cd418` | `ef 21 00 f1` | subs x15,x15,#0x8 | `FALL_THROUGH`
<a id="insn-004cd41c"></a> `004cd41c` | `20 1c 20 2e` | eor v0.8B,v1.8B,v0.8B | `FALL_THROUGH`
<a id="insn-004cd420"></a> `004cd420` | `20 85 00 fc` | str d0,[x9], #0x8 | `FALL_THROUGH`
<a id="insn-004cd424"></a> `004cd424` | `61 ff ff 54` | b.ne 0x004cd410 | `CONDITIONAL_JUMP`
<a id="insn-004cd428"></a> `004cd428` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-004cd42c"></a> `004cd42c` | `01 eb ff 54` | b.ne 0x004cd18c | `CONDITIONAL_JUMP`
<a id="insn-004cd430"></a> `004cd430` | `5d ff ff 17` | b 0x004cd1a4 | `UNCONDITIONAL_JUMP`
<a id="insn-004cd434"></a> `004cd434` | `4e 01 7d 92` | and x14,x10,#0x8 | `FALL_THROUGH`
<a id="insn-004cd438"></a> `004cd438` | `4b 09 40 92` | and x11,x10,#0x7 | `FALL_THROUGH`
<a id="insn-004cd43c"></a> `004cd43c` | `0c 01 0e 8b` | add x12,x8,x14 | `FALL_THROUGH`
<a id="insn-004cd440"></a> `004cd440` | `2d 01 0e 8b` | add x13,x9,x14 | `FALL_THROUGH`
<a id="insn-004cd444"></a> `004cd444` | `ef 03 0e aa` | mov x15,x14 | `FALL_THROUGH`
<a id="insn-004cd448"></a> `004cd448` | `00 85 40 fc` | ldr d0,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-004cd44c"></a> `004cd44c` | `21 01 40 fd` | ldr d1,[x9] | `FALL_THROUGH`
<a id="insn-004cd450"></a> `004cd450` | `ef 21 00 f1` | subs x15,x15,#0x8 | `FALL_THROUGH`
<a id="insn-004cd454"></a> `004cd454` | `20 1c 20 2e` | eor v0.8B,v1.8B,v0.8B | `FALL_THROUGH`
<a id="insn-004cd458"></a> `004cd458` | `20 85 00 fc` | str d0,[x9], #0x8 | `FALL_THROUGH`
<a id="insn-004cd45c"></a> `004cd45c` | `61 ff ff 54` | b.ne 0x004cd448 | `CONDITIONAL_JUMP`
<a id="insn-004cd460"></a> `004cd460` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-004cd464"></a> `004cd464` | `01 ed ff 54` | b.ne 0x004cd204 | `CONDITIONAL_JUMP`
<a id="insn-004cd468"></a> `004cd468` | `6d ff ff 17` | b 0x004cd21c | `UNCONDITIONAL_JUMP`
<a id="insn-004cd494"></a> `004cd494` | `bb 2e 1e 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004ccfdc`](#insn-004ccfdc) 範囲 `[['004ccfdc', '004cd043']]`
  - `CONDITIONAL_JUMP` [`004cd040`](#insn-004cd040) → [`004cd050`](#insn-004cd050)
  - `FALL_THROUGH` [`004cd040`](#insn-004cd040) → [`004cd044`](#insn-004cd044)
- ブロック [`004cd044`](#insn-004cd044) 範囲 `[['004cd044', '004cd04f']]`
  - `UNCONDITIONAL_JUMP` [`004cd04c`](#insn-004cd04c) → [`004cd05c`](#insn-004cd05c)
- ブロック [`004cd050`](#insn-004cd050) 範囲 `[['004cd050', '004cd053']]`
  - `CONDITIONAL_JUMP` [`004cd050`](#insn-004cd050) → [`004cd05c`](#insn-004cd05c)
  - `FALL_THROUGH` [`004cd050`](#insn-004cd050) → [`004cd054`](#insn-004cd054)
- ブロック [`004cd054`](#insn-004cd054) 範囲 `[['004cd054', '004cd05b']]`
  - `FALL_THROUGH` [`004cd058`](#insn-004cd058) → [`004cd05c`](#insn-004cd05c)
- ブロック [`004cd05c`](#insn-004cd05c) 範囲 `[['004cd05c', '004cd07f']]`
  - `CONDITIONAL_JUMP` [`004cd07c`](#insn-004cd07c) → [`004cd08c`](#insn-004cd08c)
  - `FALL_THROUGH` [`004cd07c`](#insn-004cd07c) → [`004cd080`](#insn-004cd080)
- ブロック [`004cd080`](#insn-004cd080) 範囲 `[['004cd080', '004cd08b']]`
  - `UNCONDITIONAL_JUMP` [`004cd088`](#insn-004cd088) → [`004cd098`](#insn-004cd098)
- ブロック [`004cd08c`](#insn-004cd08c) 範囲 `[['004cd08c', '004cd08f']]`
  - `CONDITIONAL_JUMP` [`004cd08c`](#insn-004cd08c) → [`004cd098`](#insn-004cd098)
  - `FALL_THROUGH` [`004cd08c`](#insn-004cd08c) → [`004cd090`](#insn-004cd090)
- ブロック [`004cd090`](#insn-004cd090) 範囲 `[['004cd090', '004cd097']]`
  - `FALL_THROUGH` [`004cd094`](#insn-004cd094) → [`004cd098`](#insn-004cd098)
- ブロック [`004cd098`](#insn-004cd098) 範囲 `[['004cd098', '004cd0a7']]`
  - `CONDITIONAL_JUMP` [`004cd0a4`](#insn-004cd0a4) → [`004cd0b0`](#insn-004cd0b0)
  - `FALL_THROUGH` [`004cd0a4`](#insn-004cd0a4) → [`004cd0a8`](#insn-004cd0a8)
- ブロック [`004cd0a8`](#insn-004cd0a8) 範囲 `[['004cd0a8', '004cd0af']]`
  - `FALL_THROUGH` [`004cd0ac`](#insn-004cd0ac) → [`004cd0b0`](#insn-004cd0b0)
- ブロック [`004cd0b0`](#insn-004cd0b0) 範囲 `[['004cd0b0', '004cd0bf']]`
  - `CONDITIONAL_JUMP` [`004cd0bc`](#insn-004cd0bc) → [`004cd0c8`](#insn-004cd0c8)
  - `FALL_THROUGH` [`004cd0bc`](#insn-004cd0bc) → [`004cd0c0`](#insn-004cd0c0)
- ブロック [`004cd0c0`](#insn-004cd0c0) 範囲 `[['004cd0c0', '004cd0c7']]`
  - `FALL_THROUGH` [`004cd0c4`](#insn-004cd0c4) → [`004cd0c8`](#insn-004cd0c8)
- ブロック [`004cd0c8`](#insn-004cd0c8) 範囲 `[['004cd0c8', '004cd0df']]`
  - `CONDITIONAL_JUMP` [`004cd0dc`](#insn-004cd0dc) → [`004cd250`](#insn-004cd250)
  - `FALL_THROUGH` [`004cd0dc`](#insn-004cd0dc) → [`004cd0e0`](#insn-004cd0e0)
- ブロック [`004cd0e0`](#insn-004cd0e0) 範囲 `[['004cd0e0', '004cd13f']]`
  - `CONDITIONAL_JUMP` [`004cd13c`](#insn-004cd13c) → [`004cd15c`](#insn-004cd15c)
  - `FALL_THROUGH` [`004cd13c`](#insn-004cd13c) → [`004cd140`](#insn-004cd140)
- ブロック [`004cd140`](#insn-004cd140) 範囲 `[['004cd140', '004cd15b']]`
  - `CONDITIONAL_JUMP` [`004cd158`](#insn-004cd158) → [`004cd140`](#insn-004cd140)
  - `FALL_THROUGH` [`004cd158`](#insn-004cd158) → [`004cd15c`](#insn-004cd15c)
- ブロック [`004cd15c`](#insn-004cd15c) 範囲 `[['004cd15c', '004cd15f']]`
  - `CONDITIONAL_JUMP` [`004cd15c`](#insn-004cd15c) → [`004cd1a4`](#insn-004cd1a4)
  - `FALL_THROUGH` [`004cd15c`](#insn-004cd15c) → [`004cd160`](#insn-004cd160)
- ブロック [`004cd160`](#insn-004cd160) 範囲 `[['004cd160', '004cd167']]`
  - `CONDITIONAL_JUMP` [`004cd164`](#insn-004cd164) → [`004cd180`](#insn-004cd180)
  - `FALL_THROUGH` [`004cd164`](#insn-004cd164) → [`004cd168`](#insn-004cd168)
- ブロック [`004cd168`](#insn-004cd168) 範囲 `[['004cd168', '004cd173']]`
  - `CONDITIONAL_JUMP` [`004cd170`](#insn-004cd170) → [`004cd3fc`](#insn-004cd3fc)
  - `FALL_THROUGH` [`004cd170`](#insn-004cd170) → [`004cd174`](#insn-004cd174)
- ブロック [`004cd174`](#insn-004cd174) 範囲 `[['004cd174', '004cd17f']]`
  - `CONDITIONAL_JUMP` [`004cd17c`](#insn-004cd17c) → [`004cd3fc`](#insn-004cd3fc)
  - `FALL_THROUGH` [`004cd17c`](#insn-004cd17c) → [`004cd180`](#insn-004cd180)
- ブロック [`004cd180`](#insn-004cd180) 範囲 `[['004cd180', '004cd18b']]`
  - `FALL_THROUGH` [`004cd188`](#insn-004cd188) → [`004cd18c`](#insn-004cd18c)
- ブロック [`004cd18c`](#insn-004cd18c) 範囲 `[['004cd18c', '004cd1a3']]`
  - `CONDITIONAL_JUMP` [`004cd1a0`](#insn-004cd1a0) → [`004cd18c`](#insn-004cd18c)
  - `FALL_THROUGH` [`004cd1a0`](#insn-004cd1a0) → [`004cd1a4`](#insn-004cd1a4)
- ブロック [`004cd1a4`](#insn-004cd1a4) 範囲 `[['004cd1a4', '004cd1b7']]`
  - `CONDITIONAL_JUMP` [`004cd1b4`](#insn-004cd1b4) → [`004cd1d4`](#insn-004cd1d4)
  - `FALL_THROUGH` [`004cd1b4`](#insn-004cd1b4) → [`004cd1b8`](#insn-004cd1b8)
- ブロック [`004cd1b8`](#insn-004cd1b8) 範囲 `[['004cd1b8', '004cd1d3']]`
  - `CONDITIONAL_JUMP` [`004cd1d0`](#insn-004cd1d0) → [`004cd1b8`](#insn-004cd1b8)
  - `FALL_THROUGH` [`004cd1d0`](#insn-004cd1d0) → [`004cd1d4`](#insn-004cd1d4)
- ブロック [`004cd1d4`](#insn-004cd1d4) 範囲 `[['004cd1d4', '004cd1d7']]`
  - `CONDITIONAL_JUMP` [`004cd1d4`](#insn-004cd1d4) → [`004cd21c`](#insn-004cd21c)
  - `FALL_THROUGH` [`004cd1d4`](#insn-004cd1d4) → [`004cd1d8`](#insn-004cd1d8)
- ブロック [`004cd1d8`](#insn-004cd1d8) 範囲 `[['004cd1d8', '004cd1df']]`
  - `CONDITIONAL_JUMP` [`004cd1dc`](#insn-004cd1dc) → [`004cd1f8`](#insn-004cd1f8)
  - `FALL_THROUGH` [`004cd1dc`](#insn-004cd1dc) → [`004cd1e0`](#insn-004cd1e0)
- ブロック [`004cd1e0`](#insn-004cd1e0) 範囲 `[['004cd1e0', '004cd1eb']]`
  - `CONDITIONAL_JUMP` [`004cd1e8`](#insn-004cd1e8) → [`004cd434`](#insn-004cd434)
  - `FALL_THROUGH` [`004cd1e8`](#insn-004cd1e8) → [`004cd1ec`](#insn-004cd1ec)
- ブロック [`004cd1ec`](#insn-004cd1ec) 範囲 `[['004cd1ec', '004cd1f7']]`
  - `CONDITIONAL_JUMP` [`004cd1f4`](#insn-004cd1f4) → [`004cd434`](#insn-004cd434)
  - `FALL_THROUGH` [`004cd1f4`](#insn-004cd1f4) → [`004cd1f8`](#insn-004cd1f8)
- ブロック [`004cd1f8`](#insn-004cd1f8) 範囲 `[['004cd1f8', '004cd203']]`
  - `FALL_THROUGH` [`004cd200`](#insn-004cd200) → [`004cd204`](#insn-004cd204)
- ブロック [`004cd204`](#insn-004cd204) 範囲 `[['004cd204', '004cd21b']]`
  - `CONDITIONAL_JUMP` [`004cd218`](#insn-004cd218) → [`004cd204`](#insn-004cd204)
  - `FALL_THROUGH` [`004cd218`](#insn-004cd218) → [`004cd21c`](#insn-004cd21c)
- ブロック [`004cd21c`](#insn-004cd21c) 範囲 `[['004cd21c', '004cd223']]`
  - `CONDITIONAL_JUMP` [`004cd220`](#insn-004cd220) → [`004cd348`](#insn-004cd348)
  - `FALL_THROUGH` [`004cd220`](#insn-004cd220) → [`004cd224`](#insn-004cd224)
- ブロック [`004cd224`](#insn-004cd224) 範囲 `[['004cd224', '004cd24f']]`
  - `UNCONDITIONAL_JUMP` [`004cd24c`](#insn-004cd24c) → [`004cd348`](#insn-004cd348)
- ブロック [`004cd250`](#insn-004cd250) 範囲 `[['004cd250', '004cd25b']]`
  - `CONDITIONAL_JUMP` [`004cd258`](#insn-004cd258) → [`004cd288`](#insn-004cd288)
  - `FALL_THROUGH` [`004cd258`](#insn-004cd258) → [`004cd25c`](#insn-004cd25c)
- ブロック [`004cd25c`](#insn-004cd25c) 範囲 `[['004cd25c', '004cd263']]`
  - `FALL_THROUGH` [`004cd260`](#insn-004cd260) → [`004cd264`](#insn-004cd264)
- ブロック [`004cd264`](#insn-004cd264) 範囲 `[['004cd264', '004cd27f']]`
  - `CONDITIONAL_JUMP` [`004cd27c`](#insn-004cd27c) → [`004cd264`](#insn-004cd264)
  - `FALL_THROUGH` [`004cd27c`](#insn-004cd27c) → [`004cd280`](#insn-004cd280)
- ブロック [`004cd280`](#insn-004cd280) 範囲 `[['004cd280', '004cd283']]`
  - `CONDITIONAL_JUMP` [`004cd280`](#insn-004cd280) → [`004cd294`](#insn-004cd294)
  - `FALL_THROUGH` [`004cd280`](#insn-004cd280) → [`004cd284`](#insn-004cd284)
- ブロック [`004cd284`](#insn-004cd284) 範囲 `[['004cd284', '004cd287']]`
  - `UNCONDITIONAL_JUMP` [`004cd284`](#insn-004cd284) → [`004cd2d8`](#insn-004cd2d8)
- ブロック [`004cd288`](#insn-004cd288) 範囲 `[['004cd288', '004cd293']]`
  - `CONDITIONAL_JUMP` [`004cd290`](#insn-004cd290) → [`004cd2d8`](#insn-004cd2d8)
  - `FALL_THROUGH` [`004cd290`](#insn-004cd290) → [`004cd294`](#insn-004cd294)
- ブロック [`004cd294`](#insn-004cd294) 範囲 `[['004cd294', '004cd29b']]`
  - `CONDITIONAL_JUMP` [`004cd298`](#insn-004cd298) → [`004cd2b4`](#insn-004cd2b4)
  - `FALL_THROUGH` [`004cd298`](#insn-004cd298) → [`004cd29c`](#insn-004cd29c)
- ブロック [`004cd29c`](#insn-004cd29c) 範囲 `[['004cd29c', '004cd2a7']]`
  - `CONDITIONAL_JUMP` [`004cd2a4`](#insn-004cd2a4) → [`004cd38c`](#insn-004cd38c)
  - `FALL_THROUGH` [`004cd2a4`](#insn-004cd2a4) → [`004cd2a8`](#insn-004cd2a8)
- ブロック [`004cd2a8`](#insn-004cd2a8) 範囲 `[['004cd2a8', '004cd2b3']]`
  - `CONDITIONAL_JUMP` [`004cd2b0`](#insn-004cd2b0) → [`004cd38c`](#insn-004cd38c)
  - `FALL_THROUGH` [`004cd2b0`](#insn-004cd2b0) → [`004cd2b4`](#insn-004cd2b4)
- ブロック [`004cd2b4`](#insn-004cd2b4) 範囲 `[['004cd2b4', '004cd2bf']]`
  - `FALL_THROUGH` [`004cd2bc`](#insn-004cd2bc) → [`004cd2c0`](#insn-004cd2c0)
- ブロック [`004cd2c0`](#insn-004cd2c0) 範囲 `[['004cd2c0', '004cd2d7']]`
  - `CONDITIONAL_JUMP` [`004cd2d4`](#insn-004cd2d4) → [`004cd2c0`](#insn-004cd2c0)
  - `FALL_THROUGH` [`004cd2d4`](#insn-004cd2d4) → [`004cd2d8`](#insn-004cd2d8)
- ブロック [`004cd2d8`](#insn-004cd2d8) 範囲 `[['004cd2d8', '004cd2e3']]`
  - `CONDITIONAL_JUMP` [`004cd2e0`](#insn-004cd2e0) → [`004cd300`](#insn-004cd300)
  - `FALL_THROUGH` [`004cd2e0`](#insn-004cd2e0) → [`004cd2e4`](#insn-004cd2e4)
- ブロック [`004cd2e4`](#insn-004cd2e4) 範囲 `[['004cd2e4', '004cd2ff']]`
  - `CONDITIONAL_JUMP` [`004cd2fc`](#insn-004cd2fc) → [`004cd2e4`](#insn-004cd2e4)
  - `FALL_THROUGH` [`004cd2fc`](#insn-004cd2fc) → [`004cd300`](#insn-004cd300)
- ブロック [`004cd300`](#insn-004cd300) 範囲 `[['004cd300', '004cd303']]`
  - `CONDITIONAL_JUMP` [`004cd300`](#insn-004cd300) → [`004cd348`](#insn-004cd348)
  - `FALL_THROUGH` [`004cd300`](#insn-004cd300) → [`004cd304`](#insn-004cd304)
- ブロック [`004cd304`](#insn-004cd304) 範囲 `[['004cd304', '004cd30b']]`
  - `CONDITIONAL_JUMP` [`004cd308`](#insn-004cd308) → [`004cd324`](#insn-004cd324)
  - `FALL_THROUGH` [`004cd308`](#insn-004cd308) → [`004cd30c`](#insn-004cd30c)
- ブロック [`004cd30c`](#insn-004cd30c) 範囲 `[['004cd30c', '004cd317']]`
  - `CONDITIONAL_JUMP` [`004cd314`](#insn-004cd314) → [`004cd3c4`](#insn-004cd3c4)
  - `FALL_THROUGH` [`004cd314`](#insn-004cd314) → [`004cd318`](#insn-004cd318)
- ブロック [`004cd318`](#insn-004cd318) 範囲 `[['004cd318', '004cd323']]`
  - `CONDITIONAL_JUMP` [`004cd320`](#insn-004cd320) → [`004cd3c4`](#insn-004cd3c4)
  - `FALL_THROUGH` [`004cd320`](#insn-004cd320) → [`004cd324`](#insn-004cd324)
- ブロック [`004cd324`](#insn-004cd324) 範囲 `[['004cd324', '004cd32f']]`
  - `FALL_THROUGH` [`004cd32c`](#insn-004cd32c) → [`004cd330`](#insn-004cd330)
- ブロック [`004cd330`](#insn-004cd330) 範囲 `[['004cd330', '004cd347']]`
  - `CONDITIONAL_JUMP` [`004cd344`](#insn-004cd344) → [`004cd330`](#insn-004cd330)
  - `FALL_THROUGH` [`004cd344`](#insn-004cd344) → [`004cd348`](#insn-004cd348)
- ブロック [`004cd348`](#insn-004cd348) 範囲 `[['004cd348', '004cd36f']]`
  - `CONDITIONAL_JUMP` [`004cd36c`](#insn-004cd36c) → [`004cd494`](#insn-004cd494)
  - `FALL_THROUGH` [`004cd36c`](#insn-004cd36c) → [`004cd370`](#insn-004cd370)
- ブロック [`004cd370`](#insn-004cd370) 範囲 `[['004cd370', '004cd38b']]`
- ブロック [`004cd38c`](#insn-004cd38c) 範囲 `[['004cd38c', '004cd39f']]`
  - `FALL_THROUGH` [`004cd39c`](#insn-004cd39c) → [`004cd3a0`](#insn-004cd3a0)
- ブロック [`004cd3a0`](#insn-004cd3a0) 範囲 `[['004cd3a0', '004cd3b7']]`
  - `CONDITIONAL_JUMP` [`004cd3b4`](#insn-004cd3b4) → [`004cd3a0`](#insn-004cd3a0)
  - `FALL_THROUGH` [`004cd3b4`](#insn-004cd3b4) → [`004cd3b8`](#insn-004cd3b8)
- ブロック [`004cd3b8`](#insn-004cd3b8) 範囲 `[['004cd3b8', '004cd3bf']]`
  - `CONDITIONAL_JUMP` [`004cd3bc`](#insn-004cd3bc) → [`004cd2c0`](#insn-004cd2c0)
  - `FALL_THROUGH` [`004cd3bc`](#insn-004cd3bc) → [`004cd3c0`](#insn-004cd3c0)
- ブロック [`004cd3c0`](#insn-004cd3c0) 範囲 `[['004cd3c0', '004cd3c3']]`
  - `UNCONDITIONAL_JUMP` [`004cd3c0`](#insn-004cd3c0) → [`004cd2d8`](#insn-004cd2d8)
- ブロック [`004cd3c4`](#insn-004cd3c4) 範囲 `[['004cd3c4', '004cd3d7']]`
  - `FALL_THROUGH` [`004cd3d4`](#insn-004cd3d4) → [`004cd3d8`](#insn-004cd3d8)
- ブロック [`004cd3d8`](#insn-004cd3d8) 範囲 `[['004cd3d8', '004cd3ef']]`
  - `CONDITIONAL_JUMP` [`004cd3ec`](#insn-004cd3ec) → [`004cd3d8`](#insn-004cd3d8)
  - `FALL_THROUGH` [`004cd3ec`](#insn-004cd3ec) → [`004cd3f0`](#insn-004cd3f0)
- ブロック [`004cd3f0`](#insn-004cd3f0) 範囲 `[['004cd3f0', '004cd3f7']]`
  - `CONDITIONAL_JUMP` [`004cd3f4`](#insn-004cd3f4) → [`004cd330`](#insn-004cd330)
  - `FALL_THROUGH` [`004cd3f4`](#insn-004cd3f4) → [`004cd3f8`](#insn-004cd3f8)
- ブロック [`004cd3f8`](#insn-004cd3f8) 範囲 `[['004cd3f8', '004cd3fb']]`
  - `UNCONDITIONAL_JUMP` [`004cd3f8`](#insn-004cd3f8) → [`004cd348`](#insn-004cd348)
- ブロック [`004cd3fc`](#insn-004cd3fc) 範囲 `[['004cd3fc', '004cd40f']]`
  - `FALL_THROUGH` [`004cd40c`](#insn-004cd40c) → [`004cd410`](#insn-004cd410)
- ブロック [`004cd410`](#insn-004cd410) 範囲 `[['004cd410', '004cd427']]`
  - `CONDITIONAL_JUMP` [`004cd424`](#insn-004cd424) → [`004cd410`](#insn-004cd410)
  - `FALL_THROUGH` [`004cd424`](#insn-004cd424) → [`004cd428`](#insn-004cd428)
- ブロック [`004cd428`](#insn-004cd428) 範囲 `[['004cd428', '004cd42f']]`
  - `CONDITIONAL_JUMP` [`004cd42c`](#insn-004cd42c) → [`004cd18c`](#insn-004cd18c)
  - `FALL_THROUGH` [`004cd42c`](#insn-004cd42c) → [`004cd430`](#insn-004cd430)
- ブロック [`004cd430`](#insn-004cd430) 範囲 `[['004cd430', '004cd433']]`
  - `UNCONDITIONAL_JUMP` [`004cd430`](#insn-004cd430) → [`004cd1a4`](#insn-004cd1a4)
- ブロック [`004cd434`](#insn-004cd434) 範囲 `[['004cd434', '004cd447']]`
  - `FALL_THROUGH` [`004cd444`](#insn-004cd444) → [`004cd448`](#insn-004cd448)
- ブロック [`004cd448`](#insn-004cd448) 範囲 `[['004cd448', '004cd45f']]`
  - `CONDITIONAL_JUMP` [`004cd45c`](#insn-004cd45c) → [`004cd448`](#insn-004cd448)
  - `FALL_THROUGH` [`004cd45c`](#insn-004cd45c) → [`004cd460`](#insn-004cd460)
- ブロック [`004cd460`](#insn-004cd460) 範囲 `[['004cd460', '004cd467']]`
  - `CONDITIONAL_JUMP` [`004cd464`](#insn-004cd464) → [`004cd204`](#insn-004cd204)
  - `FALL_THROUGH` [`004cd464`](#insn-004cd464) → [`004cd468`](#insn-004cd468)
- ブロック [`004cd468`](#insn-004cd468) 範囲 `[['004cd468', '004cd46b']]`
  - `UNCONDITIONAL_JUMP` [`004cd468`](#insn-004cd468) → [`004cd21c`](#insn-004cd21c)
- ブロック [`004cd494`](#insn-004cd494) 範囲 `[['004cd494', '004cd497']]`

## 命令位置別の参照

- [`004ccfe0`](#insn-004ccfe0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccfe4`](#insn-004ccfe4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccfe8`](#insn-004ccfe8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccfec`](#insn-004ccfec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccff0`](#insn-004ccff0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd00c`](#insn-004cd00c) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd040`](#insn-004cd040) → [`004cd050`](#insn-004cd050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd048`](#insn-004cd048) → [`0054084c`](../00540/0054084c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0054084c` · 推定シンボル `None` · 推定型 `None`
- [`004cd04c`](#insn-004cd04c) → [`004cd05c`](#insn-004cd05c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd050`](#insn-004cd050) → [`004cd05c`](#insn-004cd05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd07c`](#insn-004cd07c) → [`004cd08c`](#insn-004cd08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd084`](#insn-004cd084) → [`0054084c`](../00540/0054084c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0054084c` · 推定シンボル `None` · 推定型 `None`
- [`004cd088`](#insn-004cd088) → [`004cd098`](#insn-004cd098) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd08c`](#insn-004cd08c) → [`004cd098`](#insn-004cd098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd0a4`](#insn-004cd0a4) → [`004cd0b0`](#insn-004cd0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd0ac`](#insn-004cd0ac) → [`00c59130`](../00c59/00c59130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59130` · 推定シンボル `None` · 推定型 `None`
- [`004cd0bc`](#insn-004cd0bc) → [`004cd0c8`](#insn-004cd0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd0c4`](#insn-004cd0c4) → [`00c59130`](../00c59/00c59130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59130` · 推定シンボル `None` · 推定型 `None`
- [`004cd0dc`](#insn-004cd0dc) → [`004cd250`](#insn-004cd250) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd114`](#insn-004cd114) → [`004b3868`](../004b3/004b3868.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004b3868` · 推定シンボル `None` · 推定型 `None`
- [`004cd11c`](#insn-004cd11c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd12c`](#insn-004cd12c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd13c`](#insn-004cd13c) → [`004cd15c`](#insn-004cd15c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd158`](#insn-004cd158) → [`004cd140`](#insn-004cd140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd15c`](#insn-004cd15c) → [`004cd1a4`](#insn-004cd1a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd164`](#insn-004cd164) → [`004cd180`](#insn-004cd180) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd170`](#insn-004cd170) → [`004cd3fc`](#insn-004cd3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd17c`](#insn-004cd17c) → [`004cd3fc`](#insn-004cd3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd1a0`](#insn-004cd1a0) → [`004cd18c`](#insn-004cd18c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd1a4`](#insn-004cd1a4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd1b4`](#insn-004cd1b4) → [`004cd1d4`](#insn-004cd1d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd1d0`](#insn-004cd1d0) → [`004cd1b8`](#insn-004cd1b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd1d4`](#insn-004cd1d4) → [`004cd21c`](#insn-004cd21c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd1dc`](#insn-004cd1dc) → [`004cd1f8`](#insn-004cd1f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd1e8`](#insn-004cd1e8) → [`004cd434`](#insn-004cd434) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd1f4`](#insn-004cd1f4) → [`004cd434`](#insn-004cd434) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd218`](#insn-004cd218) → [`004cd204`](#insn-004cd204) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd21c`](#insn-004cd21c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd220`](#insn-004cd220) → [`004cd348`](#insn-004cd348) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd224`](#insn-004cd224) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd228`](#insn-004cd228) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd230`](#insn-004cd230) → `00c687d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cd240`](#insn-004cd240) → [`0112b058`](../0112b/0112b058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112b058` · 推定シンボル `None` · 推定型 `None`
- [`004cd248`](#insn-004cd248) → [`00c59700`](../00c59/00c59700.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59700` · 推定シンボル `None` · 推定型 `None`
- [`004cd24c`](#insn-004cd24c) → [`004cd348`](#insn-004cd348) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd258`](#insn-004cd258) → [`004cd288`](#insn-004cd288) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd27c`](#insn-004cd27c) → [`004cd264`](#insn-004cd264) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd280`](#insn-004cd280) → [`004cd294`](#insn-004cd294) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd284`](#insn-004cd284) → [`004cd2d8`](#insn-004cd2d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd290`](#insn-004cd290) → [`004cd2d8`](#insn-004cd2d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd298`](#insn-004cd298) → [`004cd2b4`](#insn-004cd2b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd2a4`](#insn-004cd2a4) → [`004cd38c`](#insn-004cd38c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd2b0`](#insn-004cd2b0) → [`004cd38c`](#insn-004cd38c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd2d4`](#insn-004cd2d4) → [`004cd2c0`](#insn-004cd2c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd2e0`](#insn-004cd2e0) → [`004cd300`](#insn-004cd300) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd2fc`](#insn-004cd2fc) → [`004cd2e4`](#insn-004cd2e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd300`](#insn-004cd300) → [`004cd348`](#insn-004cd348) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd308`](#insn-004cd308) → [`004cd324`](#insn-004cd324) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd314`](#insn-004cd314) → [`004cd3c4`](#insn-004cd3c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd320`](#insn-004cd320) → [`004cd3c4`](#insn-004cd3c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd344`](#insn-004cd344) → [`004cd330`](#insn-004cd330) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd364`](#insn-004cd364) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd36c`](#insn-004cd36c) → [`004cd494`](#insn-004cd494) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd370`](#insn-004cd370) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd374`](#insn-004cd374) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd378`](#insn-004cd378) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd37c`](#insn-004cd37c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd380`](#insn-004cd380) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd3b4`](#insn-004cd3b4) → [`004cd3a0`](#insn-004cd3a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd3bc`](#insn-004cd3bc) → [`004cd2c0`](#insn-004cd2c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd3c0`](#insn-004cd3c0) → [`004cd2d8`](#insn-004cd2d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd3ec`](#insn-004cd3ec) → [`004cd3d8`](#insn-004cd3d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd3f4`](#insn-004cd3f4) → [`004cd330`](#insn-004cd330) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd3f8`](#insn-004cd3f8) → [`004cd348`](#insn-004cd348) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd424`](#insn-004cd424) → [`004cd410`](#insn-004cd410) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd42c`](#insn-004cd42c) → [`004cd18c`](#insn-004cd18c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd430`](#insn-004cd430) → [`004cd1a4`](#insn-004cd1a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd45c`](#insn-004cd45c) → [`004cd448`](#insn-004cd448) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd464`](#insn-004cd464) → [`004cd204`](#insn-004cd204) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd468`](#insn-004cd468) → [`004cd21c`](#insn-004cd21c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd494`](#insn-004cd494) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004ccfe0`](#insn-004ccfe0)

~~~json
{
  "source": "004ccfe0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccfe4`](#insn-004ccfe4)

~~~json
{
  "source": "004ccfe4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccfe8`](#insn-004ccfe8)

~~~json
{
  "source": "004ccfe8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccfec`](#insn-004ccfec)

~~~json
{
  "source": "004ccfec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccff0`](#insn-004ccff0)

~~~json
{
  "source": "004ccff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd00c`](#insn-004cd00c)

~~~json
{
  "source": "004cd00c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd040`](#insn-004cd040)

~~~json
{
  "source": "004cd040",
  "target": "004cd050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd048`](#insn-004cd048)

~~~json
{
  "source": "004cd048",
  "target": "0054084c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cd04c`](#insn-004cd04c)

~~~json
{
  "source": "004cd04c",
  "target": "004cd05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd050`](#insn-004cd050)

~~~json
{
  "source": "004cd050",
  "target": "004cd05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd07c`](#insn-004cd07c)

~~~json
{
  "source": "004cd07c",
  "target": "004cd08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd084`](#insn-004cd084)

~~~json
{
  "source": "004cd084",
  "target": "0054084c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cd088`](#insn-004cd088)

~~~json
{
  "source": "004cd088",
  "target": "004cd098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd08c`](#insn-004cd08c)

~~~json
{
  "source": "004cd08c",
  "target": "004cd098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd0a4`](#insn-004cd0a4)

~~~json
{
  "source": "004cd0a4",
  "target": "004cd0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd0ac`](#insn-004cd0ac)

~~~json
{
  "source": "004cd0ac",
  "target": "00c59130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cd0bc`](#insn-004cd0bc)

~~~json
{
  "source": "004cd0bc",
  "target": "004cd0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd0c4`](#insn-004cd0c4)

~~~json
{
  "source": "004cd0c4",
  "target": "00c59130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cd0dc`](#insn-004cd0dc)

~~~json
{
  "source": "004cd0dc",
  "target": "004cd250",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd114`](#insn-004cd114)

~~~json
{
  "source": "004cd114",
  "target": "004b3868",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cd11c`](#insn-004cd11c)

~~~json
{
  "source": "004cd11c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd12c`](#insn-004cd12c)

~~~json
{
  "source": "004cd12c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd13c`](#insn-004cd13c)

~~~json
{
  "source": "004cd13c",
  "target": "004cd15c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd158`](#insn-004cd158)

~~~json
{
  "source": "004cd158",
  "target": "004cd140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd15c`](#insn-004cd15c)

~~~json
{
  "source": "004cd15c",
  "target": "004cd1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd164`](#insn-004cd164)

~~~json
{
  "source": "004cd164",
  "target": "004cd180",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd170`](#insn-004cd170)

~~~json
{
  "source": "004cd170",
  "target": "004cd3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd17c`](#insn-004cd17c)

~~~json
{
  "source": "004cd17c",
  "target": "004cd3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd1a0`](#insn-004cd1a0)

~~~json
{
  "source": "004cd1a0",
  "target": "004cd18c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd1a4`](#insn-004cd1a4)

~~~json
{
  "source": "004cd1a4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd1b4`](#insn-004cd1b4)

~~~json
{
  "source": "004cd1b4",
  "target": "004cd1d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd1d0`](#insn-004cd1d0)

~~~json
{
  "source": "004cd1d0",
  "target": "004cd1b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd1d4`](#insn-004cd1d4)

~~~json
{
  "source": "004cd1d4",
  "target": "004cd21c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd1dc`](#insn-004cd1dc)

~~~json
{
  "source": "004cd1dc",
  "target": "004cd1f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd1e8`](#insn-004cd1e8)

~~~json
{
  "source": "004cd1e8",
  "target": "004cd434",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd1f4`](#insn-004cd1f4)

~~~json
{
  "source": "004cd1f4",
  "target": "004cd434",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd218`](#insn-004cd218)

~~~json
{
  "source": "004cd218",
  "target": "004cd204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd21c`](#insn-004cd21c)

~~~json
{
  "source": "004cd21c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd220`](#insn-004cd220)

~~~json
{
  "source": "004cd220",
  "target": "004cd348",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd224`](#insn-004cd224)

~~~json
{
  "source": "004cd224",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd228`](#insn-004cd228)

~~~json
{
  "source": "004cd228",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd230`](#insn-004cd230)

~~~json
{
  "source": "004cd230",
  "target": "00c687d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c687d8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cd240`](#insn-004cd240)

~~~json
{
  "source": "004cd240",
  "target": "0112b058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cd248`](#insn-004cd248)

~~~json
{
  "source": "004cd248",
  "target": "00c59700",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cd24c`](#insn-004cd24c)

~~~json
{
  "source": "004cd24c",
  "target": "004cd348",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd258`](#insn-004cd258)

~~~json
{
  "source": "004cd258",
  "target": "004cd288",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd27c`](#insn-004cd27c)

~~~json
{
  "source": "004cd27c",
  "target": "004cd264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd280`](#insn-004cd280)

~~~json
{
  "source": "004cd280",
  "target": "004cd294",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd284`](#insn-004cd284)

~~~json
{
  "source": "004cd284",
  "target": "004cd2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd290`](#insn-004cd290)

~~~json
{
  "source": "004cd290",
  "target": "004cd2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd298`](#insn-004cd298)

~~~json
{
  "source": "004cd298",
  "target": "004cd2b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd2a4`](#insn-004cd2a4)

~~~json
{
  "source": "004cd2a4",
  "target": "004cd38c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd2b0`](#insn-004cd2b0)

~~~json
{
  "source": "004cd2b0",
  "target": "004cd38c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd2d4`](#insn-004cd2d4)

~~~json
{
  "source": "004cd2d4",
  "target": "004cd2c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd2e0`](#insn-004cd2e0)

~~~json
{
  "source": "004cd2e0",
  "target": "004cd300",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd2fc`](#insn-004cd2fc)

~~~json
{
  "source": "004cd2fc",
  "target": "004cd2e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd300`](#insn-004cd300)

~~~json
{
  "source": "004cd300",
  "target": "004cd348",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd308`](#insn-004cd308)

~~~json
{
  "source": "004cd308",
  "target": "004cd324",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd314`](#insn-004cd314)

~~~json
{
  "source": "004cd314",
  "target": "004cd3c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd320`](#insn-004cd320)

~~~json
{
  "source": "004cd320",
  "target": "004cd3c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd344`](#insn-004cd344)

~~~json
{
  "source": "004cd344",
  "target": "004cd330",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd364`](#insn-004cd364)

~~~json
{
  "source": "004cd364",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd36c`](#insn-004cd36c)

~~~json
{
  "source": "004cd36c",
  "target": "004cd494",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd370`](#insn-004cd370)

~~~json
{
  "source": "004cd370",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd374`](#insn-004cd374)

~~~json
{
  "source": "004cd374",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd378`](#insn-004cd378)

~~~json
{
  "source": "004cd378",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd37c`](#insn-004cd37c)

~~~json
{
  "source": "004cd37c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd380`](#insn-004cd380)

~~~json
{
  "source": "004cd380",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd3b4`](#insn-004cd3b4)

~~~json
{
  "source": "004cd3b4",
  "target": "004cd3a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd3bc`](#insn-004cd3bc)

~~~json
{
  "source": "004cd3bc",
  "target": "004cd2c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd3c0`](#insn-004cd3c0)

~~~json
{
  "source": "004cd3c0",
  "target": "004cd2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd3ec`](#insn-004cd3ec)

~~~json
{
  "source": "004cd3ec",
  "target": "004cd3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd3f4`](#insn-004cd3f4)

~~~json
{
  "source": "004cd3f4",
  "target": "004cd330",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd3f8`](#insn-004cd3f8)

~~~json
{
  "source": "004cd3f8",
  "target": "004cd348",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd424`](#insn-004cd424)

~~~json
{
  "source": "004cd424",
  "target": "004cd410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd42c`](#insn-004cd42c)

~~~json
{
  "source": "004cd42c",
  "target": "004cd18c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd430`](#insn-004cd430)

~~~json
{
  "source": "004cd430",
  "target": "004cd1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd45c`](#insn-004cd45c)

~~~json
{
  "source": "004cd45c",
  "target": "004cd448",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd464`](#insn-004cd464)

~~~json
{
  "source": "004cd464",
  "target": "004cd204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd468`](#insn-004cd468)

~~~json
{
  "source": "004cd468",
  "target": "004cd21c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd494`](#insn-004cd494)

~~~json
{
  "source": "004cd494",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
