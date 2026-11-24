# 004cccbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `004ccc7c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004ccc7c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0002.md#compare-d43bc9584be5c06350f72f81f5935044)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `004ccfdc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cc/004ccfdc.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0002.md#compare-5828aa812ead223c940c77d81252794c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004cccbc",
  "name": "_ZN5Botan4HMAC12key_scheduleEPKhm",
  "size": 1172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "04a330061d6dda5f1db8fcf115d9ee6b74711993ac94b758fb5876dfbe517d8f",
  "source_text_sha256": "04a330061d6dda5f1db8fcf115d9ee6b74711993ac94b758fb5876dfbe517d8f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004cccbc",
        "004cd14b"
      ],
      [
        "004cd174",
        "004cd177"
      ]
    ],
    "bytes_sha256": "2ce3ea90bbc9d034d4a6c7018ad950bb1032b01579fe99d62a1bc3120c0cc189",
    "instruction_count": 293,
    "instruction_bytes": 1172,
    "body_bytes": 1172,
    "indirect": 9,
    "unresolved": 8
  }
}
~~~

## 呼び出し元

- [00c59240](../00c59/00c59240.md)

## 呼び出し先

- [004b3548](../004b3/004b3548.md)
- [0054052c](../00540/0054052c.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58160](../00c58/00c58160.md)
- [00c58730](../00c58/00c58730.md)
- [0112a058](../0112a/0112a058.md)

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
    FUN_0054052c(plVar13,uVar3 - uVar8);
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
    FUN_0054052c(plVar12,uVar3 - uVar8);
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
    FUN_004b3548(&local_70,uVar4);
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
        if (bVar2) goto LAB_004cce84;
      }
      do {
        uVar3 = uVar3 - 1;
        *pbVar10 = *pbVar10 ^ *pbVar6;
        pbVar6 = pbVar6 + 1;
        pbVar10 = pbVar10 + 1;
      } while (uVar3 != 0);
    }
LAB_004cce84:
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
        if (bVar2) goto LAB_004ccefc;
      }
      do {
        uVar3 = uVar3 - 1;
        *pbVar10 = *pbVar10 ^ *pbVar6;
        pbVar6 = pbVar6 + 1;
        pbVar10 = pbVar10 + 1;
      } while (uVar3 != 0);
    }
LAB_004ccefc:
    if (local_70 != (byte *)0x0) {
      local_68 = local_70;
      (*(code *)PTR_memset_00c67808)(local_70,0,local_60 - (long)local_70);
      free(local_70);
    }
    goto LAB_004cd028;
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
      if (bVar2) goto LAB_004ccfb8;
    }
    do {
      uVar3 = uVar3 - 1;
      *pbVar10 = *pbVar10 ^ *pbVar6;
      pbVar6 = pbVar6 + 1;
      pbVar10 = pbVar10 + 1;
    } while (uVar3 != 0);
  }
LAB_004ccfb8:
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
      if (bVar2) goto LAB_004cd028;
    }
    do {
      param_3 = param_3 - 1;
      *pbVar10 = *pbVar10 ^ *param_2;
      param_2 = param_2 + 1;
      pbVar10 = pbVar10 + 1;
    } while (param_3 != 0);
  }
LAB_004cd028:
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
<a id="insn-004cccbc"></a> `004cccbc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-004cccc0"></a> `004cccc0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004cccc4"></a> `004cccc4` | `f9 1b 00 f9` | str x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004cccc8"></a> `004cccc8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004ccccc"></a> `004ccccc` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004cccd0"></a> `004cccd0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004cccd4"></a> `004cccd4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004cccd8"></a> `004cccd8` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004cccdc"></a> `004cccdc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004ccce0"></a> `004ccce0` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-004ccce4"></a> `004ccce4` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-004ccce8"></a> `004ccce8` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-004cccec"></a> `004cccec` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cccf0"></a> `004cccf0` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004cccf4"></a> `004cccf4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004cccf8"></a> `004cccf8` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-004cccfc"></a> `004cccfc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004ccd00"></a> `004ccd00` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004ccd04"></a> `004ccd04` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004ccd08"></a> `004ccd08` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-004ccd0c"></a> `004ccd0c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004ccd10"></a> `004ccd10` | `f7 03 13 aa` | mov x23,x19 | `FALL_THROUGH`
<a id="insn-004ccd14"></a> `004ccd14` | `e8 a6 c1 a9` | ldp x8,x9,[x23, #0x18]! | `FALL_THROUGH`
<a id="insn-004ccd18"></a> `004ccd18` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004ccd1c"></a> `004ccd1c` | `01 00 09 eb` | subs x1,x0,x9 | `FALL_THROUGH`
<a id="insn-004ccd20"></a> `004ccd20` | `89 00 00 54` | b.ls 0x004ccd30 | `CONDITIONAL_JUMP`
<a id="insn-004ccd24"></a> `004ccd24` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-004ccd28"></a> `004ccd28` | `01 ce 01 94` | bl 0x0054052c | `UNCONDITIONAL_CALL`
<a id="insn-004ccd2c"></a> `004ccd2c` | `04 00 00 14` | b 0x004ccd3c | `UNCONDITIONAL_JUMP`
<a id="insn-004ccd30"></a> `004ccd30` | `62 00 00 54` | b.cs 0x004ccd3c | `CONDITIONAL_JUMP`
<a id="insn-004ccd34"></a> `004ccd34` | `08 01 00 8b` | add x8,x8,x0 | `FALL_THROUGH`
<a id="insn-004ccd38"></a> `004ccd38` | `68 12 00 f9` | str x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-004ccd3c"></a> `004ccd3c` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004ccd40"></a> `004ccd40` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004ccd44"></a> `004ccd44` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-004ccd48"></a> `004ccd48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004ccd4c"></a> `004ccd4c` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-004ccd50"></a> `004ccd50` | `88 26 c3 a9` | ldp x8,x9,[x20, #0x30]! | `FALL_THROUGH`
<a id="insn-004ccd54"></a> `004ccd54` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004ccd58"></a> `004ccd58` | `01 00 09 eb` | subs x1,x0,x9 | `FALL_THROUGH`
<a id="insn-004ccd5c"></a> `004ccd5c` | `89 00 00 54` | b.ls 0x004ccd6c | `CONDITIONAL_JUMP`
<a id="insn-004ccd60"></a> `004ccd60` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004ccd64"></a> `004ccd64` | `f2 cd 01 94` | bl 0x0054052c | `UNCONDITIONAL_CALL`
<a id="insn-004ccd68"></a> `004ccd68` | `04 00 00 14` | b 0x004ccd78 | `UNCONDITIONAL_JUMP`
<a id="insn-004ccd6c"></a> `004ccd6c` | `62 00 00 54` | b.cs 0x004ccd78 | `CONDITIONAL_JUMP`
<a id="insn-004ccd70"></a> `004ccd70` | `08 01 00 8b` | add x8,x8,x0 | `FALL_THROUGH`
<a id="insn-004ccd74"></a> `004ccd74` | `68 1e 00 f9` | str x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-004ccd78"></a> `004ccd78` | `60 a2 41 a9` | ldp x0,x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-004ccd7c"></a> `004ccd7c` | `02 01 00 cb` | sub x2,x8,x0 | `FALL_THROUGH`
<a id="insn-004ccd80"></a> `004ccd80` | `5f 04 00 f1` | cmp x2,#0x1 | `FALL_THROUGH`
<a id="insn-004ccd84"></a> `004ccd84` | `6b 00 00 54` | b.lt 0x004ccd90 | `CONDITIONAL_JUMP`
<a id="insn-004ccd88"></a> `004ccd88` | `c1 06 80 52` | mov w1,#0x36 | `FALL_THROUGH`
<a id="insn-004ccd8c"></a> `004ccd8c` | `f5 2c 1e 94` | bl 0x00c58160 | `UNCONDITIONAL_CALL`
<a id="insn-004ccd90"></a> `004ccd90` | `60 22 43 a9` | ldp x0,x8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-004ccd94"></a> `004ccd94` | `02 01 00 cb` | sub x2,x8,x0 | `FALL_THROUGH`
<a id="insn-004ccd98"></a> `004ccd98` | `5f 04 00 f1` | cmp x2,#0x1 | `FALL_THROUGH`
<a id="insn-004ccd9c"></a> `004ccd9c` | `6b 00 00 54` | b.lt 0x004ccda8 | `CONDITIONAL_JUMP`
<a id="insn-004ccda0"></a> `004ccda0` | `81 0b 80 52` | mov w1,#0x5c | `FALL_THROUGH`
<a id="insn-004ccda4"></a> `004ccda4` | `ef 2c 1e 94` | bl 0x00c58160 | `UNCONDITIONAL_CALL`
<a id="insn-004ccda8"></a> `004ccda8` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004ccdac"></a> `004ccdac` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004ccdb0"></a> `004ccdb0` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-004ccdb4"></a> `004ccdb4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004ccdb8"></a> `004ccdb8` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-004ccdbc"></a> `004ccdbc` | `a2 0b 00 54` | b.cs 0x004ccf30 | `CONDITIONAL_JUMP`
<a id="insn-004ccdc0"></a> `004ccdc0` | `78 0a 40 f9` | ldr x24,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004ccdc4"></a> `004ccdc4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-004ccdc8"></a> `004ccdc8` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-004ccdcc"></a> `004ccdcc` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-004ccdd0"></a> `004ccdd0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-004ccdd4"></a> `004ccdd4` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-004ccdd8"></a> `004ccdd8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004ccddc"></a> `004ccddc` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-004ccde0"></a> `004ccde0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-004ccde4"></a> `004ccde4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-004ccde8"></a> `004ccde8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004ccdec"></a> `004ccdec` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-004ccdf0"></a> `004ccdf0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004ccdf4"></a> `004ccdf4` | `d5 99 ff 97` | bl 0x004b3548 | `UNCONDITIONAL_CALL`
<a id="insn-004ccdf8"></a> `004ccdf8` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-004ccdfc"></a> `004ccdfc` | `e1 03 40 f9` | ldr x1,[sp] | `FALL_THROUGH`
<a id="insn-004cce00"></a> `004cce00` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-004cce04"></a> `004cce04` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-004cce08"></a> `004cce08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cce0c"></a> `004cce0c` | `e8 27 40 a9` | ldp x8,x9,[sp] | `FALL_THROUGH`
<a id="insn-004cce10"></a> `004cce10` | `2a 01 08 cb` | sub x10,x9,x8 | `FALL_THROUGH`
<a id="insn-004cce14"></a> `004cce14` | `e9 02 40 f9` | ldr x9,[x23] | `FALL_THROUGH`
<a id="insn-004cce18"></a> `004cce18` | `5f 41 00 f1` | cmp x10,#0x10 | `FALL_THROUGH`
<a id="insn-004cce1c"></a> `004cce1c` | `03 01 00 54` | b.cc 0x004cce3c | `CONDITIONAL_JUMP`
<a id="insn-004cce20"></a> `004cce20` | `00 05 c1 3c` | ldr q0,[x8], #0x10 | `FALL_THROUGH`
<a id="insn-004cce24"></a> `004cce24` | `21 01 c0 3d` | ldr q1,[x9] | `FALL_THROUGH`
<a id="insn-004cce28"></a> `004cce28` | `4a 41 00 d1` | sub x10,x10,#0x10 | `FALL_THROUGH`
<a id="insn-004cce2c"></a> `004cce2c` | `20 1c 20 6e` | eor v0.16B,v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-004cce30"></a> `004cce30` | `5f 3d 00 f1` | cmp x10,#0xf | `FALL_THROUGH`
<a id="insn-004cce34"></a> `004cce34` | `20 05 81 3c` | str q0,[x9], #0x10 | `FALL_THROUGH`
<a id="insn-004cce38"></a> `004cce38` | `48 ff ff 54` | b.hi 0x004cce20 | `CONDITIONAL_JUMP`
<a id="insn-004cce3c"></a> `004cce3c` | `4a 02 00 b4` | cbz x10,0x004cce84 | `CONDITIONAL_JUMP`
<a id="insn-004cce40"></a> `004cce40` | `5f 21 00 f1` | cmp x10,#0x8 | `FALL_THROUGH`
<a id="insn-004cce44"></a> `004cce44` | `e3 00 00 54` | b.cc 0x004cce60 | `CONDITIONAL_JUMP`
<a id="insn-004cce48"></a> `004cce48` | `0b 01 0a 8b` | add x11,x8,x10 | `FALL_THROUGH`
<a id="insn-004cce4c"></a> `004cce4c` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-004cce50"></a> `004cce50` | `62 14 00 54` | b.cs 0x004cd0dc | `CONDITIONAL_JUMP`
<a id="insn-004cce54"></a> `004cce54` | `2b 01 0a 8b` | add x11,x9,x10 | `FALL_THROUGH`
<a id="insn-004cce58"></a> `004cce58` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-004cce5c"></a> `004cce5c` | `02 14 00 54` | b.cs 0x004cd0dc | `CONDITIONAL_JUMP`
<a id="insn-004cce60"></a> `004cce60` | `eb 03 0a aa` | mov x11,x10 | `FALL_THROUGH`
<a id="insn-004cce64"></a> `004cce64` | `ec 03 08 aa` | mov x12,x8 | `FALL_THROUGH`
<a id="insn-004cce68"></a> `004cce68` | `ed 03 09 aa` | mov x13,x9 | `FALL_THROUGH`
<a id="insn-004cce6c"></a> `004cce6c` | `88 15 40 38` | ldrb w8,[x12], #0x1 | `FALL_THROUGH`
<a id="insn-004cce70"></a> `004cce70` | `a9 01 40 39` | ldrb w9,[x13] | `FALL_THROUGH`
<a id="insn-004cce74"></a> `004cce74` | `6b 05 00 f1` | subs x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-004cce78"></a> `004cce78` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-004cce7c"></a> `004cce7c` | `a8 15 00 38` | strb w8,[x13], #0x1 | `FALL_THROUGH`
<a id="insn-004cce80"></a> `004cce80` | `61 ff ff 54` | b.ne 0x004cce6c | `CONDITIONAL_JUMP`
<a id="insn-004cce84"></a> `004cce84` | `e8 27 40 a9` | ldp x8,x9,[sp] | `FALL_THROUGH`
<a id="insn-004cce88"></a> `004cce88` | `2a 01 08 cb` | sub x10,x9,x8 | `FALL_THROUGH`
<a id="insn-004cce8c"></a> `004cce8c` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-004cce90"></a> `004cce90` | `5f 41 00 f1` | cmp x10,#0x10 | `FALL_THROUGH`
<a id="insn-004cce94"></a> `004cce94` | `03 01 00 54` | b.cc 0x004cceb4 | `CONDITIONAL_JUMP`
<a id="insn-004cce98"></a> `004cce98` | `00 05 c1 3c` | ldr q0,[x8], #0x10 | `FALL_THROUGH`
<a id="insn-004cce9c"></a> `004cce9c` | `21 01 c0 3d` | ldr q1,[x9] | `FALL_THROUGH`
<a id="insn-004ccea0"></a> `004ccea0` | `4a 41 00 d1` | sub x10,x10,#0x10 | `FALL_THROUGH`
<a id="insn-004ccea4"></a> `004ccea4` | `20 1c 20 6e` | eor v0.16B,v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-004ccea8"></a> `004ccea8` | `5f 3d 00 f1` | cmp x10,#0xf | `FALL_THROUGH`
<a id="insn-004cceac"></a> `004cceac` | `20 05 81 3c` | str q0,[x9], #0x10 | `FALL_THROUGH`
<a id="insn-004cceb0"></a> `004cceb0` | `48 ff ff 54` | b.hi 0x004cce98 | `CONDITIONAL_JUMP`
<a id="insn-004cceb4"></a> `004cceb4` | `4a 02 00 b4` | cbz x10,0x004ccefc | `CONDITIONAL_JUMP`
<a id="insn-004cceb8"></a> `004cceb8` | `5f 21 00 f1` | cmp x10,#0x8 | `FALL_THROUGH`
<a id="insn-004ccebc"></a> `004ccebc` | `e3 00 00 54` | b.cc 0x004cced8 | `CONDITIONAL_JUMP`
<a id="insn-004ccec0"></a> `004ccec0` | `0b 01 0a 8b` | add x11,x8,x10 | `FALL_THROUGH`
<a id="insn-004ccec4"></a> `004ccec4` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-004ccec8"></a> `004ccec8` | `62 12 00 54` | b.cs 0x004cd114 | `CONDITIONAL_JUMP`
<a id="insn-004ccecc"></a> `004ccecc` | `2b 01 0a 8b` | add x11,x9,x10 | `FALL_THROUGH`
<a id="insn-004cced0"></a> `004cced0` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-004cced4"></a> `004cced4` | `02 12 00 54` | b.cs 0x004cd114 | `CONDITIONAL_JUMP`
<a id="insn-004cced8"></a> `004cced8` | `eb 03 0a aa` | mov x11,x10 | `FALL_THROUGH`
<a id="insn-004ccedc"></a> `004ccedc` | `ec 03 08 aa` | mov x12,x8 | `FALL_THROUGH`
<a id="insn-004ccee0"></a> `004ccee0` | `ed 03 09 aa` | mov x13,x9 | `FALL_THROUGH`
<a id="insn-004ccee4"></a> `004ccee4` | `88 15 40 38` | ldrb w8,[x12], #0x1 | `FALL_THROUGH`
<a id="insn-004ccee8"></a> `004ccee8` | `a9 01 40 39` | ldrb w9,[x13] | `FALL_THROUGH`
<a id="insn-004cceec"></a> `004cceec` | `6b 05 00 f1` | subs x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-004ccef0"></a> `004ccef0` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-004ccef4"></a> `004ccef4` | `a8 15 00 38` | strb w8,[x13], #0x1 | `FALL_THROUGH`
<a id="insn-004ccef8"></a> `004ccef8` | `61 ff ff 54` | b.ne 0x004ccee4 | `CONDITIONAL_JUMP`
<a id="insn-004ccefc"></a> `004ccefc` | `f4 03 40 f9` | ldr x20,[sp] | `FALL_THROUGH`
<a id="insn-004ccf00"></a> `004ccf00` | `54 09 00 b4` | cbz x20,0x004cd028 | `CONDITIONAL_JUMP`
<a id="insn-004ccf04"></a> `004ccf04` | `f4 07 00 f9` | str x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004ccf08"></a> `004ccf08` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ccf0c"></a> `004ccf0c` | `c9 3c 00 f0` | adrp x9,0xc67000 | `FALL_THROUGH`
<a id="insn-004ccf10"></a> `004ccf10` | `29 05 44 f9` | ldr x9,[x9, #0x808] | `FALL_THROUGH`
<a id="insn-004ccf14"></a> `004ccf14` | `02 01 14 cb` | sub x2,x8,x20 | `FALL_THROUGH`
<a id="insn-004ccf18"></a> `004ccf18` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004ccf1c"></a> `004ccf1c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004ccf20"></a> `004ccf20` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004ccf24"></a> `004ccf24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004ccf28"></a> `004ccf28` | `02 2e 1e 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-004ccf2c"></a> `004ccf2c` | `3f 00 00 14` | b 0x004cd028 | `UNCONDITIONAL_JUMP`
<a id="insn-004ccf30"></a> `004ccf30` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-004ccf34"></a> `004ccf34` | `bf 42 00 f1` | cmp x21,#0x10 | `FALL_THROUGH`
<a id="insn-004ccf38"></a> `004ccf38` | `83 01 00 54` | b.cc 0x004ccf68 | `CONDITIONAL_JUMP`
<a id="insn-004ccf3c"></a> `004ccf3c` | `ea 03 15 aa` | mov x10,x21 | `FALL_THROUGH`
<a id="insn-004ccf40"></a> `004ccf40` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-004ccf44"></a> `004ccf44` | `20 05 c1 3c` | ldr q0,[x9], #0x10 | `FALL_THROUGH`
<a id="insn-004ccf48"></a> `004ccf48` | `01 01 c0 3d` | ldr q1,[x8] | `FALL_THROUGH`
<a id="insn-004ccf4c"></a> `004ccf4c` | `4a 41 00 d1` | sub x10,x10,#0x10 | `FALL_THROUGH`
<a id="insn-004ccf50"></a> `004ccf50` | `20 1c 20 6e` | eor v0.16B,v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-004ccf54"></a> `004ccf54` | `5f 3d 00 f1` | cmp x10,#0xf | `FALL_THROUGH`
<a id="insn-004ccf58"></a> `004ccf58` | `00 05 81 3c` | str q0,[x8], #0x10 | `FALL_THROUGH`
<a id="insn-004ccf5c"></a> `004ccf5c` | `48 ff ff 54` | b.hi 0x004ccf44 | `CONDITIONAL_JUMP`
<a id="insn-004ccf60"></a> `004ccf60` | `aa 00 00 b5` | cbnz x10,0x004ccf74 | `CONDITIONAL_JUMP`
<a id="insn-004ccf64"></a> `004ccf64` | `15 00 00 14` | b 0x004ccfb8 | `UNCONDITIONAL_JUMP`
<a id="insn-004ccf68"></a> `004ccf68` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-004ccf6c"></a> `004ccf6c` | `ea 03 15 aa` | mov x10,x21 | `FALL_THROUGH`
<a id="insn-004ccf70"></a> `004ccf70` | `4a 02 00 b4` | cbz x10,0x004ccfb8 | `CONDITIONAL_JUMP`
<a id="insn-004ccf74"></a> `004ccf74` | `5f 21 00 f1` | cmp x10,#0x8 | `FALL_THROUGH`
<a id="insn-004ccf78"></a> `004ccf78` | `e3 00 00 54` | b.cc 0x004ccf94 | `CONDITIONAL_JUMP`
<a id="insn-004ccf7c"></a> `004ccf7c` | `2b 01 0a 8b` | add x11,x9,x10 | `FALL_THROUGH`
<a id="insn-004ccf80"></a> `004ccf80` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-004ccf84"></a> `004ccf84` | `42 07 00 54` | b.cs 0x004cd06c | `CONDITIONAL_JUMP`
<a id="insn-004ccf88"></a> `004ccf88` | `0b 01 0a 8b` | add x11,x8,x10 | `FALL_THROUGH`
<a id="insn-004ccf8c"></a> `004ccf8c` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-004ccf90"></a> `004ccf90` | `e2 06 00 54` | b.cs 0x004cd06c | `CONDITIONAL_JUMP`
<a id="insn-004ccf94"></a> `004ccf94` | `eb 03 0a aa` | mov x11,x10 | `FALL_THROUGH`
<a id="insn-004ccf98"></a> `004ccf98` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-004ccf9c"></a> `004ccf9c` | `ed 03 08 aa` | mov x13,x8 | `FALL_THROUGH`
<a id="insn-004ccfa0"></a> `004ccfa0` | `88 15 40 38` | ldrb w8,[x12], #0x1 | `FALL_THROUGH`
<a id="insn-004ccfa4"></a> `004ccfa4` | `a9 01 40 39` | ldrb w9,[x13] | `FALL_THROUGH`
<a id="insn-004ccfa8"></a> `004ccfa8` | `6b 05 00 f1` | subs x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-004ccfac"></a> `004ccfac` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-004ccfb0"></a> `004ccfb0` | `a8 15 00 38` | strb w8,[x13], #0x1 | `FALL_THROUGH`
<a id="insn-004ccfb4"></a> `004ccfb4` | `61 ff ff 54` | b.ne 0x004ccfa0 | `CONDITIONAL_JUMP`
<a id="insn-004ccfb8"></a> `004ccfb8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-004ccfbc"></a> `004ccfbc` | `bf 42 00 f1` | cmp x21,#0x10 | `FALL_THROUGH`
<a id="insn-004ccfc0"></a> `004ccfc0` | `03 01 00 54` | b.cc 0x004ccfe0 | `CONDITIONAL_JUMP`
<a id="insn-004ccfc4"></a> `004ccfc4` | `c0 06 c1 3c` | ldr q0,[x22], #0x10 | `FALL_THROUGH`
<a id="insn-004ccfc8"></a> `004ccfc8` | `01 01 c0 3d` | ldr q1,[x8] | `FALL_THROUGH`
<a id="insn-004ccfcc"></a> `004ccfcc` | `b5 42 00 d1` | sub x21,x21,#0x10 | `FALL_THROUGH`
<a id="insn-004ccfd0"></a> `004ccfd0` | `20 1c 20 6e` | eor v0.16B,v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-004ccfd4"></a> `004ccfd4` | `bf 3e 00 f1` | cmp x21,#0xf | `FALL_THROUGH`
<a id="insn-004ccfd8"></a> `004ccfd8` | `00 05 81 3c` | str q0,[x8], #0x10 | `FALL_THROUGH`
<a id="insn-004ccfdc"></a> `004ccfdc` | `48 ff ff 54` | b.hi 0x004ccfc4 | `CONDITIONAL_JUMP`
<a id="insn-004ccfe0"></a> `004ccfe0` | `55 02 00 b4` | cbz x21,0x004cd028 | `CONDITIONAL_JUMP`
<a id="insn-004ccfe4"></a> `004ccfe4` | `bf 22 00 f1` | cmp x21,#0x8 | `FALL_THROUGH`
<a id="insn-004ccfe8"></a> `004ccfe8` | `e3 00 00 54` | b.cc 0x004cd004 | `CONDITIONAL_JUMP`
<a id="insn-004ccfec"></a> `004ccfec` | `c9 02 15 8b` | add x9,x22,x21 | `FALL_THROUGH`
<a id="insn-004ccff0"></a> `004ccff0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004ccff4"></a> `004ccff4` | `82 05 00 54` | b.cs 0x004cd0a4 | `CONDITIONAL_JUMP`
<a id="insn-004ccff8"></a> `004ccff8` | `09 01 15 8b` | add x9,x8,x21 | `FALL_THROUGH`
<a id="insn-004ccffc"></a> `004ccffc` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-004cd000"></a> `004cd000` | `22 05 00 54` | b.cs 0x004cd0a4 | `CONDITIONAL_JUMP`
<a id="insn-004cd004"></a> `004cd004` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-004cd008"></a> `004cd008` | `ea 03 16 aa` | mov x10,x22 | `FALL_THROUGH`
<a id="insn-004cd00c"></a> `004cd00c` | `eb 03 08 aa` | mov x11,x8 | `FALL_THROUGH`
<a id="insn-004cd010"></a> `004cd010` | `48 15 40 38` | ldrb w8,[x10], #0x1 | `FALL_THROUGH`
<a id="insn-004cd014"></a> `004cd014` | `6c 01 40 39` | ldrb w12,[x11] | `FALL_THROUGH`
<a id="insn-004cd018"></a> `004cd018` | `29 05 00 f1` | subs x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004cd01c"></a> `004cd01c` | `88 01 08 4a` | eor w8,w12,w8 | `FALL_THROUGH`
<a id="insn-004cd020"></a> `004cd020` | `68 15 00 38` | strb w8,[x11], #0x1 | `FALL_THROUGH`
<a id="insn-004cd024"></a> `004cd024` | `61 ff ff 54` | b.ne 0x004cd010 | `CONDITIONAL_JUMP`
<a id="insn-004cd028"></a> `004cd028` | `60 06 41 a9` | ldp x0,x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004cd02c"></a> `004cd02c` | `69 12 40 f9` | ldr x9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-004cd030"></a> `004cd030` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004cd034"></a> `004cd034` | `22 01 01 cb` | sub x2,x9,x1 | `FALL_THROUGH`
<a id="insn-004cd038"></a> `004cd038` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-004cd03c"></a> `004cd03c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cd040"></a> `004cd040` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-004cd044"></a> `004cd044` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cd048"></a> `004cd048` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004cd04c"></a> `004cd04c` | `41 09 00 54` | b.ne 0x004cd174 | `CONDITIONAL_JUMP`
<a id="insn-004cd050"></a> `004cd050` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004cd054"></a> `004cd054` | `f9 1b 40 f9` | ldr x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004cd058"></a> `004cd058` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004cd05c"></a> `004cd05c` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004cd060"></a> `004cd060` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004cd064"></a> `004cd064` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-004cd068"></a> `004cd068` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004cd06c"></a> `004cd06c` | `4e 01 7d 92` | and x14,x10,#0x8 | `FALL_THROUGH`
<a id="insn-004cd070"></a> `004cd070` | `4b 09 40 92` | and x11,x10,#0x7 | `FALL_THROUGH`
<a id="insn-004cd074"></a> `004cd074` | `2c 01 0e 8b` | add x12,x9,x14 | `FALL_THROUGH`
<a id="insn-004cd078"></a> `004cd078` | `0d 01 0e 8b` | add x13,x8,x14 | `FALL_THROUGH`
<a id="insn-004cd07c"></a> `004cd07c` | `ef 03 0e aa` | mov x15,x14 | `FALL_THROUGH`
<a id="insn-004cd080"></a> `004cd080` | `20 85 40 fc` | ldr d0,[x9], #0x8 | `FALL_THROUGH`
<a id="insn-004cd084"></a> `004cd084` | `01 01 40 fd` | ldr d1,[x8] | `FALL_THROUGH`
<a id="insn-004cd088"></a> `004cd088` | `ef 21 00 f1` | subs x15,x15,#0x8 | `FALL_THROUGH`
<a id="insn-004cd08c"></a> `004cd08c` | `20 1c 20 2e` | eor v0.8B,v1.8B,v0.8B | `FALL_THROUGH`
<a id="insn-004cd090"></a> `004cd090` | `00 85 00 fc` | str d0,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-004cd094"></a> `004cd094` | `61 ff ff 54` | b.ne 0x004cd080 | `CONDITIONAL_JUMP`
<a id="insn-004cd098"></a> `004cd098` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-004cd09c"></a> `004cd09c` | `21 f8 ff 54` | b.ne 0x004ccfa0 | `CONDITIONAL_JUMP`
<a id="insn-004cd0a0"></a> `004cd0a0` | `c6 ff ff 17` | b 0x004ccfb8 | `UNCONDITIONAL_JUMP`
<a id="insn-004cd0a4"></a> `004cd0a4` | `ac 02 7d 92` | and x12,x21,#0x8 | `FALL_THROUGH`
<a id="insn-004cd0a8"></a> `004cd0a8` | `a9 0a 40 92` | and x9,x21,#0x7 | `FALL_THROUGH`
<a id="insn-004cd0ac"></a> `004cd0ac` | `ca 02 0c 8b` | add x10,x22,x12 | `FALL_THROUGH`
<a id="insn-004cd0b0"></a> `004cd0b0` | `0b 01 0c 8b` | add x11,x8,x12 | `FALL_THROUGH`
<a id="insn-004cd0b4"></a> `004cd0b4` | `ed 03 0c aa` | mov x13,x12 | `FALL_THROUGH`
<a id="insn-004cd0b8"></a> `004cd0b8` | `c0 86 40 fc` | ldr d0,[x22], #0x8 | `FALL_THROUGH`
<a id="insn-004cd0bc"></a> `004cd0bc` | `01 01 40 fd` | ldr d1,[x8] | `FALL_THROUGH`
<a id="insn-004cd0c0"></a> `004cd0c0` | `ad 21 00 f1` | subs x13,x13,#0x8 | `FALL_THROUGH`
<a id="insn-004cd0c4"></a> `004cd0c4` | `20 1c 20 2e` | eor v0.8B,v1.8B,v0.8B | `FALL_THROUGH`
<a id="insn-004cd0c8"></a> `004cd0c8` | `00 85 00 fc` | str d0,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-004cd0cc"></a> `004cd0cc` | `61 ff ff 54` | b.ne 0x004cd0b8 | `CONDITIONAL_JUMP`
<a id="insn-004cd0d0"></a> `004cd0d0` | `bf 02 0c eb` | cmp x21,x12 | `FALL_THROUGH`
<a id="insn-004cd0d4"></a> `004cd0d4` | `e1 f9 ff 54` | b.ne 0x004cd010 | `CONDITIONAL_JUMP`
<a id="insn-004cd0d8"></a> `004cd0d8` | `d4 ff ff 17` | b 0x004cd028 | `UNCONDITIONAL_JUMP`
<a id="insn-004cd0dc"></a> `004cd0dc` | `4e 01 7d 92` | and x14,x10,#0x8 | `FALL_THROUGH`
<a id="insn-004cd0e0"></a> `004cd0e0` | `4b 09 40 92` | and x11,x10,#0x7 | `FALL_THROUGH`
<a id="insn-004cd0e4"></a> `004cd0e4` | `0c 01 0e 8b` | add x12,x8,x14 | `FALL_THROUGH`
<a id="insn-004cd0e8"></a> `004cd0e8` | `2d 01 0e 8b` | add x13,x9,x14 | `FALL_THROUGH`
<a id="insn-004cd0ec"></a> `004cd0ec` | `ef 03 0e aa` | mov x15,x14 | `FALL_THROUGH`
<a id="insn-004cd0f0"></a> `004cd0f0` | `00 85 40 fc` | ldr d0,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-004cd0f4"></a> `004cd0f4` | `21 01 40 fd` | ldr d1,[x9] | `FALL_THROUGH`
<a id="insn-004cd0f8"></a> `004cd0f8` | `ef 21 00 f1` | subs x15,x15,#0x8 | `FALL_THROUGH`
<a id="insn-004cd0fc"></a> `004cd0fc` | `20 1c 20 2e` | eor v0.8B,v1.8B,v0.8B | `FALL_THROUGH`
<a id="insn-004cd100"></a> `004cd100` | `20 85 00 fc` | str d0,[x9], #0x8 | `FALL_THROUGH`
<a id="insn-004cd104"></a> `004cd104` | `61 ff ff 54` | b.ne 0x004cd0f0 | `CONDITIONAL_JUMP`
<a id="insn-004cd108"></a> `004cd108` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-004cd10c"></a> `004cd10c` | `01 eb ff 54` | b.ne 0x004cce6c | `CONDITIONAL_JUMP`
<a id="insn-004cd110"></a> `004cd110` | `5d ff ff 17` | b 0x004cce84 | `UNCONDITIONAL_JUMP`
<a id="insn-004cd114"></a> `004cd114` | `4e 01 7d 92` | and x14,x10,#0x8 | `FALL_THROUGH`
<a id="insn-004cd118"></a> `004cd118` | `4b 09 40 92` | and x11,x10,#0x7 | `FALL_THROUGH`
<a id="insn-004cd11c"></a> `004cd11c` | `0c 01 0e 8b` | add x12,x8,x14 | `FALL_THROUGH`
<a id="insn-004cd120"></a> `004cd120` | `2d 01 0e 8b` | add x13,x9,x14 | `FALL_THROUGH`
<a id="insn-004cd124"></a> `004cd124` | `ef 03 0e aa` | mov x15,x14 | `FALL_THROUGH`
<a id="insn-004cd128"></a> `004cd128` | `00 85 40 fc` | ldr d0,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-004cd12c"></a> `004cd12c` | `21 01 40 fd` | ldr d1,[x9] | `FALL_THROUGH`
<a id="insn-004cd130"></a> `004cd130` | `ef 21 00 f1` | subs x15,x15,#0x8 | `FALL_THROUGH`
<a id="insn-004cd134"></a> `004cd134` | `20 1c 20 2e` | eor v0.8B,v1.8B,v0.8B | `FALL_THROUGH`
<a id="insn-004cd138"></a> `004cd138` | `20 85 00 fc` | str d0,[x9], #0x8 | `FALL_THROUGH`
<a id="insn-004cd13c"></a> `004cd13c` | `61 ff ff 54` | b.ne 0x004cd128 | `CONDITIONAL_JUMP`
<a id="insn-004cd140"></a> `004cd140` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-004cd144"></a> `004cd144` | `01 ed ff 54` | b.ne 0x004ccee4 | `CONDITIONAL_JUMP`
<a id="insn-004cd148"></a> `004cd148` | `6d ff ff 17` | b 0x004ccefc | `UNCONDITIONAL_JUMP`
<a id="insn-004cd174"></a> `004cd174` | `8f 2b 1e 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004cccbc`](#insn-004cccbc) 範囲 `[['004cccbc', '004ccd23']]`
  - `CONDITIONAL_JUMP` [`004ccd20`](#insn-004ccd20) → [`004ccd30`](#insn-004ccd30)
  - `FALL_THROUGH` [`004ccd20`](#insn-004ccd20) → [`004ccd24`](#insn-004ccd24)
- ブロック [`004ccd24`](#insn-004ccd24) 範囲 `[['004ccd24', '004ccd2f']]`
  - `UNCONDITIONAL_JUMP` [`004ccd2c`](#insn-004ccd2c) → [`004ccd3c`](#insn-004ccd3c)
- ブロック [`004ccd30`](#insn-004ccd30) 範囲 `[['004ccd30', '004ccd33']]`
  - `CONDITIONAL_JUMP` [`004ccd30`](#insn-004ccd30) → [`004ccd3c`](#insn-004ccd3c)
  - `FALL_THROUGH` [`004ccd30`](#insn-004ccd30) → [`004ccd34`](#insn-004ccd34)
- ブロック [`004ccd34`](#insn-004ccd34) 範囲 `[['004ccd34', '004ccd3b']]`
  - `FALL_THROUGH` [`004ccd38`](#insn-004ccd38) → [`004ccd3c`](#insn-004ccd3c)
- ブロック [`004ccd3c`](#insn-004ccd3c) 範囲 `[['004ccd3c', '004ccd5f']]`
  - `CONDITIONAL_JUMP` [`004ccd5c`](#insn-004ccd5c) → [`004ccd6c`](#insn-004ccd6c)
  - `FALL_THROUGH` [`004ccd5c`](#insn-004ccd5c) → [`004ccd60`](#insn-004ccd60)
- ブロック [`004ccd60`](#insn-004ccd60) 範囲 `[['004ccd60', '004ccd6b']]`
  - `UNCONDITIONAL_JUMP` [`004ccd68`](#insn-004ccd68) → [`004ccd78`](#insn-004ccd78)
- ブロック [`004ccd6c`](#insn-004ccd6c) 範囲 `[['004ccd6c', '004ccd6f']]`
  - `CONDITIONAL_JUMP` [`004ccd6c`](#insn-004ccd6c) → [`004ccd78`](#insn-004ccd78)
  - `FALL_THROUGH` [`004ccd6c`](#insn-004ccd6c) → [`004ccd70`](#insn-004ccd70)
- ブロック [`004ccd70`](#insn-004ccd70) 範囲 `[['004ccd70', '004ccd77']]`
  - `FALL_THROUGH` [`004ccd74`](#insn-004ccd74) → [`004ccd78`](#insn-004ccd78)
- ブロック [`004ccd78`](#insn-004ccd78) 範囲 `[['004ccd78', '004ccd87']]`
  - `CONDITIONAL_JUMP` [`004ccd84`](#insn-004ccd84) → [`004ccd90`](#insn-004ccd90)
  - `FALL_THROUGH` [`004ccd84`](#insn-004ccd84) → [`004ccd88`](#insn-004ccd88)
- ブロック [`004ccd88`](#insn-004ccd88) 範囲 `[['004ccd88', '004ccd8f']]`
  - `FALL_THROUGH` [`004ccd8c`](#insn-004ccd8c) → [`004ccd90`](#insn-004ccd90)
- ブロック [`004ccd90`](#insn-004ccd90) 範囲 `[['004ccd90', '004ccd9f']]`
  - `CONDITIONAL_JUMP` [`004ccd9c`](#insn-004ccd9c) → [`004ccda8`](#insn-004ccda8)
  - `FALL_THROUGH` [`004ccd9c`](#insn-004ccd9c) → [`004ccda0`](#insn-004ccda0)
- ブロック [`004ccda0`](#insn-004ccda0) 範囲 `[['004ccda0', '004ccda7']]`
  - `FALL_THROUGH` [`004ccda4`](#insn-004ccda4) → [`004ccda8`](#insn-004ccda8)
- ブロック [`004ccda8`](#insn-004ccda8) 範囲 `[['004ccda8', '004ccdbf']]`
  - `CONDITIONAL_JUMP` [`004ccdbc`](#insn-004ccdbc) → [`004ccf30`](#insn-004ccf30)
  - `FALL_THROUGH` [`004ccdbc`](#insn-004ccdbc) → [`004ccdc0`](#insn-004ccdc0)
- ブロック [`004ccdc0`](#insn-004ccdc0) 範囲 `[['004ccdc0', '004cce1f']]`
  - `CONDITIONAL_JUMP` [`004cce1c`](#insn-004cce1c) → [`004cce3c`](#insn-004cce3c)
  - `FALL_THROUGH` [`004cce1c`](#insn-004cce1c) → [`004cce20`](#insn-004cce20)
- ブロック [`004cce20`](#insn-004cce20) 範囲 `[['004cce20', '004cce3b']]`
  - `CONDITIONAL_JUMP` [`004cce38`](#insn-004cce38) → [`004cce20`](#insn-004cce20)
  - `FALL_THROUGH` [`004cce38`](#insn-004cce38) → [`004cce3c`](#insn-004cce3c)
- ブロック [`004cce3c`](#insn-004cce3c) 範囲 `[['004cce3c', '004cce3f']]`
  - `CONDITIONAL_JUMP` [`004cce3c`](#insn-004cce3c) → [`004cce84`](#insn-004cce84)
  - `FALL_THROUGH` [`004cce3c`](#insn-004cce3c) → [`004cce40`](#insn-004cce40)
- ブロック [`004cce40`](#insn-004cce40) 範囲 `[['004cce40', '004cce47']]`
  - `CONDITIONAL_JUMP` [`004cce44`](#insn-004cce44) → [`004cce60`](#insn-004cce60)
  - `FALL_THROUGH` [`004cce44`](#insn-004cce44) → [`004cce48`](#insn-004cce48)
- ブロック [`004cce48`](#insn-004cce48) 範囲 `[['004cce48', '004cce53']]`
  - `CONDITIONAL_JUMP` [`004cce50`](#insn-004cce50) → [`004cd0dc`](#insn-004cd0dc)
  - `FALL_THROUGH` [`004cce50`](#insn-004cce50) → [`004cce54`](#insn-004cce54)
- ブロック [`004cce54`](#insn-004cce54) 範囲 `[['004cce54', '004cce5f']]`
  - `CONDITIONAL_JUMP` [`004cce5c`](#insn-004cce5c) → [`004cd0dc`](#insn-004cd0dc)
  - `FALL_THROUGH` [`004cce5c`](#insn-004cce5c) → [`004cce60`](#insn-004cce60)
- ブロック [`004cce60`](#insn-004cce60) 範囲 `[['004cce60', '004cce6b']]`
  - `FALL_THROUGH` [`004cce68`](#insn-004cce68) → [`004cce6c`](#insn-004cce6c)
- ブロック [`004cce6c`](#insn-004cce6c) 範囲 `[['004cce6c', '004cce83']]`
  - `CONDITIONAL_JUMP` [`004cce80`](#insn-004cce80) → [`004cce6c`](#insn-004cce6c)
  - `FALL_THROUGH` [`004cce80`](#insn-004cce80) → [`004cce84`](#insn-004cce84)
- ブロック [`004cce84`](#insn-004cce84) 範囲 `[['004cce84', '004cce97']]`
  - `CONDITIONAL_JUMP` [`004cce94`](#insn-004cce94) → [`004cceb4`](#insn-004cceb4)
  - `FALL_THROUGH` [`004cce94`](#insn-004cce94) → [`004cce98`](#insn-004cce98)
- ブロック [`004cce98`](#insn-004cce98) 範囲 `[['004cce98', '004cceb3']]`
  - `CONDITIONAL_JUMP` [`004cceb0`](#insn-004cceb0) → [`004cce98`](#insn-004cce98)
  - `FALL_THROUGH` [`004cceb0`](#insn-004cceb0) → [`004cceb4`](#insn-004cceb4)
- ブロック [`004cceb4`](#insn-004cceb4) 範囲 `[['004cceb4', '004cceb7']]`
  - `CONDITIONAL_JUMP` [`004cceb4`](#insn-004cceb4) → [`004ccefc`](#insn-004ccefc)
  - `FALL_THROUGH` [`004cceb4`](#insn-004cceb4) → [`004cceb8`](#insn-004cceb8)
- ブロック [`004cceb8`](#insn-004cceb8) 範囲 `[['004cceb8', '004ccebf']]`
  - `CONDITIONAL_JUMP` [`004ccebc`](#insn-004ccebc) → [`004cced8`](#insn-004cced8)
  - `FALL_THROUGH` [`004ccebc`](#insn-004ccebc) → [`004ccec0`](#insn-004ccec0)
- ブロック [`004ccec0`](#insn-004ccec0) 範囲 `[['004ccec0', '004ccecb']]`
  - `CONDITIONAL_JUMP` [`004ccec8`](#insn-004ccec8) → [`004cd114`](#insn-004cd114)
  - `FALL_THROUGH` [`004ccec8`](#insn-004ccec8) → [`004ccecc`](#insn-004ccecc)
- ブロック [`004ccecc`](#insn-004ccecc) 範囲 `[['004ccecc', '004cced7']]`
  - `CONDITIONAL_JUMP` [`004cced4`](#insn-004cced4) → [`004cd114`](#insn-004cd114)
  - `FALL_THROUGH` [`004cced4`](#insn-004cced4) → [`004cced8`](#insn-004cced8)
- ブロック [`004cced8`](#insn-004cced8) 範囲 `[['004cced8', '004ccee3']]`
  - `FALL_THROUGH` [`004ccee0`](#insn-004ccee0) → [`004ccee4`](#insn-004ccee4)
- ブロック [`004ccee4`](#insn-004ccee4) 範囲 `[['004ccee4', '004ccefb']]`
  - `CONDITIONAL_JUMP` [`004ccef8`](#insn-004ccef8) → [`004ccee4`](#insn-004ccee4)
  - `FALL_THROUGH` [`004ccef8`](#insn-004ccef8) → [`004ccefc`](#insn-004ccefc)
- ブロック [`004ccefc`](#insn-004ccefc) 範囲 `[['004ccefc', '004ccf03']]`
  - `CONDITIONAL_JUMP` [`004ccf00`](#insn-004ccf00) → [`004cd028`](#insn-004cd028)
  - `FALL_THROUGH` [`004ccf00`](#insn-004ccf00) → [`004ccf04`](#insn-004ccf04)
- ブロック [`004ccf04`](#insn-004ccf04) 範囲 `[['004ccf04', '004ccf2f']]`
  - `UNCONDITIONAL_JUMP` [`004ccf2c`](#insn-004ccf2c) → [`004cd028`](#insn-004cd028)
- ブロック [`004ccf30`](#insn-004ccf30) 範囲 `[['004ccf30', '004ccf3b']]`
  - `CONDITIONAL_JUMP` [`004ccf38`](#insn-004ccf38) → [`004ccf68`](#insn-004ccf68)
  - `FALL_THROUGH` [`004ccf38`](#insn-004ccf38) → [`004ccf3c`](#insn-004ccf3c)
- ブロック [`004ccf3c`](#insn-004ccf3c) 範囲 `[['004ccf3c', '004ccf43']]`
  - `FALL_THROUGH` [`004ccf40`](#insn-004ccf40) → [`004ccf44`](#insn-004ccf44)
- ブロック [`004ccf44`](#insn-004ccf44) 範囲 `[['004ccf44', '004ccf5f']]`
  - `CONDITIONAL_JUMP` [`004ccf5c`](#insn-004ccf5c) → [`004ccf44`](#insn-004ccf44)
  - `FALL_THROUGH` [`004ccf5c`](#insn-004ccf5c) → [`004ccf60`](#insn-004ccf60)
- ブロック [`004ccf60`](#insn-004ccf60) 範囲 `[['004ccf60', '004ccf63']]`
  - `CONDITIONAL_JUMP` [`004ccf60`](#insn-004ccf60) → [`004ccf74`](#insn-004ccf74)
  - `FALL_THROUGH` [`004ccf60`](#insn-004ccf60) → [`004ccf64`](#insn-004ccf64)
- ブロック [`004ccf64`](#insn-004ccf64) 範囲 `[['004ccf64', '004ccf67']]`
  - `UNCONDITIONAL_JUMP` [`004ccf64`](#insn-004ccf64) → [`004ccfb8`](#insn-004ccfb8)
- ブロック [`004ccf68`](#insn-004ccf68) 範囲 `[['004ccf68', '004ccf73']]`
  - `CONDITIONAL_JUMP` [`004ccf70`](#insn-004ccf70) → [`004ccfb8`](#insn-004ccfb8)
  - `FALL_THROUGH` [`004ccf70`](#insn-004ccf70) → [`004ccf74`](#insn-004ccf74)
- ブロック [`004ccf74`](#insn-004ccf74) 範囲 `[['004ccf74', '004ccf7b']]`
  - `CONDITIONAL_JUMP` [`004ccf78`](#insn-004ccf78) → [`004ccf94`](#insn-004ccf94)
  - `FALL_THROUGH` [`004ccf78`](#insn-004ccf78) → [`004ccf7c`](#insn-004ccf7c)
- ブロック [`004ccf7c`](#insn-004ccf7c) 範囲 `[['004ccf7c', '004ccf87']]`
  - `CONDITIONAL_JUMP` [`004ccf84`](#insn-004ccf84) → [`004cd06c`](#insn-004cd06c)
  - `FALL_THROUGH` [`004ccf84`](#insn-004ccf84) → [`004ccf88`](#insn-004ccf88)
- ブロック [`004ccf88`](#insn-004ccf88) 範囲 `[['004ccf88', '004ccf93']]`
  - `CONDITIONAL_JUMP` [`004ccf90`](#insn-004ccf90) → [`004cd06c`](#insn-004cd06c)
  - `FALL_THROUGH` [`004ccf90`](#insn-004ccf90) → [`004ccf94`](#insn-004ccf94)
- ブロック [`004ccf94`](#insn-004ccf94) 範囲 `[['004ccf94', '004ccf9f']]`
  - `FALL_THROUGH` [`004ccf9c`](#insn-004ccf9c) → [`004ccfa0`](#insn-004ccfa0)
- ブロック [`004ccfa0`](#insn-004ccfa0) 範囲 `[['004ccfa0', '004ccfb7']]`
  - `CONDITIONAL_JUMP` [`004ccfb4`](#insn-004ccfb4) → [`004ccfa0`](#insn-004ccfa0)
  - `FALL_THROUGH` [`004ccfb4`](#insn-004ccfb4) → [`004ccfb8`](#insn-004ccfb8)
- ブロック [`004ccfb8`](#insn-004ccfb8) 範囲 `[['004ccfb8', '004ccfc3']]`
  - `CONDITIONAL_JUMP` [`004ccfc0`](#insn-004ccfc0) → [`004ccfe0`](#insn-004ccfe0)
  - `FALL_THROUGH` [`004ccfc0`](#insn-004ccfc0) → [`004ccfc4`](#insn-004ccfc4)
- ブロック [`004ccfc4`](#insn-004ccfc4) 範囲 `[['004ccfc4', '004ccfdf']]`
  - `CONDITIONAL_JUMP` [`004ccfdc`](#insn-004ccfdc) → [`004ccfc4`](#insn-004ccfc4)
  - `FALL_THROUGH` [`004ccfdc`](#insn-004ccfdc) → [`004ccfe0`](#insn-004ccfe0)
- ブロック [`004ccfe0`](#insn-004ccfe0) 範囲 `[['004ccfe0', '004ccfe3']]`
  - `CONDITIONAL_JUMP` [`004ccfe0`](#insn-004ccfe0) → [`004cd028`](#insn-004cd028)
  - `FALL_THROUGH` [`004ccfe0`](#insn-004ccfe0) → [`004ccfe4`](#insn-004ccfe4)
- ブロック [`004ccfe4`](#insn-004ccfe4) 範囲 `[['004ccfe4', '004ccfeb']]`
  - `CONDITIONAL_JUMP` [`004ccfe8`](#insn-004ccfe8) → [`004cd004`](#insn-004cd004)
  - `FALL_THROUGH` [`004ccfe8`](#insn-004ccfe8) → [`004ccfec`](#insn-004ccfec)
- ブロック [`004ccfec`](#insn-004ccfec) 範囲 `[['004ccfec', '004ccff7']]`
  - `CONDITIONAL_JUMP` [`004ccff4`](#insn-004ccff4) → [`004cd0a4`](#insn-004cd0a4)
  - `FALL_THROUGH` [`004ccff4`](#insn-004ccff4) → [`004ccff8`](#insn-004ccff8)
- ブロック [`004ccff8`](#insn-004ccff8) 範囲 `[['004ccff8', '004cd003']]`
  - `CONDITIONAL_JUMP` [`004cd000`](#insn-004cd000) → [`004cd0a4`](#insn-004cd0a4)
  - `FALL_THROUGH` [`004cd000`](#insn-004cd000) → [`004cd004`](#insn-004cd004)
- ブロック [`004cd004`](#insn-004cd004) 範囲 `[['004cd004', '004cd00f']]`
  - `FALL_THROUGH` [`004cd00c`](#insn-004cd00c) → [`004cd010`](#insn-004cd010)
- ブロック [`004cd010`](#insn-004cd010) 範囲 `[['004cd010', '004cd027']]`
  - `CONDITIONAL_JUMP` [`004cd024`](#insn-004cd024) → [`004cd010`](#insn-004cd010)
  - `FALL_THROUGH` [`004cd024`](#insn-004cd024) → [`004cd028`](#insn-004cd028)
- ブロック [`004cd028`](#insn-004cd028) 範囲 `[['004cd028', '004cd04f']]`
  - `CONDITIONAL_JUMP` [`004cd04c`](#insn-004cd04c) → [`004cd174`](#insn-004cd174)
  - `FALL_THROUGH` [`004cd04c`](#insn-004cd04c) → [`004cd050`](#insn-004cd050)
- ブロック [`004cd050`](#insn-004cd050) 範囲 `[['004cd050', '004cd06b']]`
- ブロック [`004cd06c`](#insn-004cd06c) 範囲 `[['004cd06c', '004cd07f']]`
  - `FALL_THROUGH` [`004cd07c`](#insn-004cd07c) → [`004cd080`](#insn-004cd080)
- ブロック [`004cd080`](#insn-004cd080) 範囲 `[['004cd080', '004cd097']]`
  - `CONDITIONAL_JUMP` [`004cd094`](#insn-004cd094) → [`004cd080`](#insn-004cd080)
  - `FALL_THROUGH` [`004cd094`](#insn-004cd094) → [`004cd098`](#insn-004cd098)
- ブロック [`004cd098`](#insn-004cd098) 範囲 `[['004cd098', '004cd09f']]`
  - `CONDITIONAL_JUMP` [`004cd09c`](#insn-004cd09c) → [`004ccfa0`](#insn-004ccfa0)
  - `FALL_THROUGH` [`004cd09c`](#insn-004cd09c) → [`004cd0a0`](#insn-004cd0a0)
- ブロック [`004cd0a0`](#insn-004cd0a0) 範囲 `[['004cd0a0', '004cd0a3']]`
  - `UNCONDITIONAL_JUMP` [`004cd0a0`](#insn-004cd0a0) → [`004ccfb8`](#insn-004ccfb8)
- ブロック [`004cd0a4`](#insn-004cd0a4) 範囲 `[['004cd0a4', '004cd0b7']]`
  - `FALL_THROUGH` [`004cd0b4`](#insn-004cd0b4) → [`004cd0b8`](#insn-004cd0b8)
- ブロック [`004cd0b8`](#insn-004cd0b8) 範囲 `[['004cd0b8', '004cd0cf']]`
  - `CONDITIONAL_JUMP` [`004cd0cc`](#insn-004cd0cc) → [`004cd0b8`](#insn-004cd0b8)
  - `FALL_THROUGH` [`004cd0cc`](#insn-004cd0cc) → [`004cd0d0`](#insn-004cd0d0)
- ブロック [`004cd0d0`](#insn-004cd0d0) 範囲 `[['004cd0d0', '004cd0d7']]`
  - `CONDITIONAL_JUMP` [`004cd0d4`](#insn-004cd0d4) → [`004cd010`](#insn-004cd010)
  - `FALL_THROUGH` [`004cd0d4`](#insn-004cd0d4) → [`004cd0d8`](#insn-004cd0d8)
- ブロック [`004cd0d8`](#insn-004cd0d8) 範囲 `[['004cd0d8', '004cd0db']]`
  - `UNCONDITIONAL_JUMP` [`004cd0d8`](#insn-004cd0d8) → [`004cd028`](#insn-004cd028)
- ブロック [`004cd0dc`](#insn-004cd0dc) 範囲 `[['004cd0dc', '004cd0ef']]`
  - `FALL_THROUGH` [`004cd0ec`](#insn-004cd0ec) → [`004cd0f0`](#insn-004cd0f0)
- ブロック [`004cd0f0`](#insn-004cd0f0) 範囲 `[['004cd0f0', '004cd107']]`
  - `CONDITIONAL_JUMP` [`004cd104`](#insn-004cd104) → [`004cd0f0`](#insn-004cd0f0)
  - `FALL_THROUGH` [`004cd104`](#insn-004cd104) → [`004cd108`](#insn-004cd108)
- ブロック [`004cd108`](#insn-004cd108) 範囲 `[['004cd108', '004cd10f']]`
  - `CONDITIONAL_JUMP` [`004cd10c`](#insn-004cd10c) → [`004cce6c`](#insn-004cce6c)
  - `FALL_THROUGH` [`004cd10c`](#insn-004cd10c) → [`004cd110`](#insn-004cd110)
- ブロック [`004cd110`](#insn-004cd110) 範囲 `[['004cd110', '004cd113']]`
  - `UNCONDITIONAL_JUMP` [`004cd110`](#insn-004cd110) → [`004cce84`](#insn-004cce84)
- ブロック [`004cd114`](#insn-004cd114) 範囲 `[['004cd114', '004cd127']]`
  - `FALL_THROUGH` [`004cd124`](#insn-004cd124) → [`004cd128`](#insn-004cd128)
- ブロック [`004cd128`](#insn-004cd128) 範囲 `[['004cd128', '004cd13f']]`
  - `CONDITIONAL_JUMP` [`004cd13c`](#insn-004cd13c) → [`004cd128`](#insn-004cd128)
  - `FALL_THROUGH` [`004cd13c`](#insn-004cd13c) → [`004cd140`](#insn-004cd140)
- ブロック [`004cd140`](#insn-004cd140) 範囲 `[['004cd140', '004cd147']]`
  - `CONDITIONAL_JUMP` [`004cd144`](#insn-004cd144) → [`004ccee4`](#insn-004ccee4)
  - `FALL_THROUGH` [`004cd144`](#insn-004cd144) → [`004cd148`](#insn-004cd148)
- ブロック [`004cd148`](#insn-004cd148) 範囲 `[['004cd148', '004cd14b']]`
  - `UNCONDITIONAL_JUMP` [`004cd148`](#insn-004cd148) → [`004ccefc`](#insn-004ccefc)
- ブロック [`004cd174`](#insn-004cd174) 範囲 `[['004cd174', '004cd177']]`

## 命令位置別の参照

- [`004cccc0`](#insn-004cccc0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cccc4`](#insn-004cccc4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cccc8`](#insn-004cccc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccccc`](#insn-004ccccc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cccd0`](#insn-004cccd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cccec`](#insn-004cccec) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccd20`](#insn-004ccd20) → [`004ccd30`](#insn-004ccd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccd28`](#insn-004ccd28) → [`0054052c`](../00540/0054052c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0054052c` · 推定シンボル `None` · 推定型 `None`
- [`004ccd2c`](#insn-004ccd2c) → [`004ccd3c`](#insn-004ccd3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccd30`](#insn-004ccd30) → [`004ccd3c`](#insn-004ccd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccd5c`](#insn-004ccd5c) → [`004ccd6c`](#insn-004ccd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccd64`](#insn-004ccd64) → [`0054052c`](../00540/0054052c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0054052c` · 推定シンボル `None` · 推定型 `None`
- [`004ccd68`](#insn-004ccd68) → [`004ccd78`](#insn-004ccd78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccd6c`](#insn-004ccd6c) → [`004ccd78`](#insn-004ccd78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccd84`](#insn-004ccd84) → [`004ccd90`](#insn-004ccd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccd8c`](#insn-004ccd8c) → [`00c58160`](../00c58/00c58160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58160` · 推定シンボル `None` · 推定型 `None`
- [`004ccd9c`](#insn-004ccd9c) → [`004ccda8`](#insn-004ccda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccda4`](#insn-004ccda4) → [`00c58160`](../00c58/00c58160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58160` · 推定シンボル `None` · 推定型 `None`
- [`004ccdbc`](#insn-004ccdbc) → [`004ccf30`](#insn-004ccf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccdf4`](#insn-004ccdf4) → [`004b3548`](../004b3/004b3548.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004b3548` · 推定シンボル `None` · 推定型 `None`
- [`004ccdfc`](#insn-004ccdfc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cce0c`](#insn-004cce0c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cce1c`](#insn-004cce1c) → [`004cce3c`](#insn-004cce3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cce38`](#insn-004cce38) → [`004cce20`](#insn-004cce20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cce3c`](#insn-004cce3c) → [`004cce84`](#insn-004cce84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cce44`](#insn-004cce44) → [`004cce60`](#insn-004cce60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cce50`](#insn-004cce50) → [`004cd0dc`](#insn-004cd0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cce5c`](#insn-004cce5c) → [`004cd0dc`](#insn-004cd0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cce80`](#insn-004cce80) → [`004cce6c`](#insn-004cce6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cce84`](#insn-004cce84) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cce94`](#insn-004cce94) → [`004cceb4`](#insn-004cceb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cceb0`](#insn-004cceb0) → [`004cce98`](#insn-004cce98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cceb4`](#insn-004cceb4) → [`004ccefc`](#insn-004ccefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccebc`](#insn-004ccebc) → [`004cced8`](#insn-004cced8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccec8`](#insn-004ccec8) → [`004cd114`](#insn-004cd114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cced4`](#insn-004cced4) → [`004cd114`](#insn-004cd114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccef8`](#insn-004ccef8) → [`004ccee4`](#insn-004ccee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccefc`](#insn-004ccefc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccf00`](#insn-004ccf00) → [`004cd028`](#insn-004cd028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccf04`](#insn-004ccf04) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccf08`](#insn-004ccf08) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccf10`](#insn-004ccf10) → `00c67808`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ccf20`](#insn-004ccf20) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004ccf28`](#insn-004ccf28) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`004ccf2c`](#insn-004ccf2c) → [`004cd028`](#insn-004cd028) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccf38`](#insn-004ccf38) → [`004ccf68`](#insn-004ccf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccf5c`](#insn-004ccf5c) → [`004ccf44`](#insn-004ccf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccf60`](#insn-004ccf60) → [`004ccf74`](#insn-004ccf74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccf64`](#insn-004ccf64) → [`004ccfb8`](#insn-004ccfb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccf70`](#insn-004ccf70) → [`004ccfb8`](#insn-004ccfb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccf78`](#insn-004ccf78) → [`004ccf94`](#insn-004ccf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccf84`](#insn-004ccf84) → [`004cd06c`](#insn-004cd06c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccf90`](#insn-004ccf90) → [`004cd06c`](#insn-004cd06c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccfb4`](#insn-004ccfb4) → [`004ccfa0`](#insn-004ccfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccfc0`](#insn-004ccfc0) → [`004ccfe0`](#insn-004ccfe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccfdc`](#insn-004ccfdc) → [`004ccfc4`](#insn-004ccfc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccfe0`](#insn-004ccfe0) → [`004cd028`](#insn-004cd028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccfe8`](#insn-004ccfe8) → [`004cd004`](#insn-004cd004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccff4`](#insn-004ccff4) → [`004cd0a4`](#insn-004cd0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd000`](#insn-004cd000) → [`004cd0a4`](#insn-004cd0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd024`](#insn-004cd024) → [`004cd010`](#insn-004cd010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd044`](#insn-004cd044) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd04c`](#insn-004cd04c) → [`004cd174`](#insn-004cd174) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd050`](#insn-004cd050) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd054`](#insn-004cd054) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd058`](#insn-004cd058) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd05c`](#insn-004cd05c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd060`](#insn-004cd060) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd094`](#insn-004cd094) → [`004cd080`](#insn-004cd080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd09c`](#insn-004cd09c) → [`004ccfa0`](#insn-004ccfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd0a0`](#insn-004cd0a0) → [`004ccfb8`](#insn-004ccfb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd0cc`](#insn-004cd0cc) → [`004cd0b8`](#insn-004cd0b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd0d4`](#insn-004cd0d4) → [`004cd010`](#insn-004cd010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd0d8`](#insn-004cd0d8) → [`004cd028`](#insn-004cd028) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd104`](#insn-004cd104) → [`004cd0f0`](#insn-004cd0f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd10c`](#insn-004cd10c) → [`004cce6c`](#insn-004cce6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd110`](#insn-004cd110) → [`004cce84`](#insn-004cce84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd13c`](#insn-004cd13c) → [`004cd128`](#insn-004cd128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd144`](#insn-004cd144) → [`004ccee4`](#insn-004ccee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd148`](#insn-004cd148) → [`004ccefc`](#insn-004ccefc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cd174`](#insn-004cd174) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004cccc0`](#insn-004cccc0)

~~~json
{
  "source": "004cccc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cccc4`](#insn-004cccc4)

~~~json
{
  "source": "004cccc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cccc8`](#insn-004cccc8)

~~~json
{
  "source": "004cccc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccccc`](#insn-004ccccc)

~~~json
{
  "source": "004ccccc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cccd0`](#insn-004cccd0)

~~~json
{
  "source": "004cccd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cccec`](#insn-004cccec)

~~~json
{
  "source": "004cccec",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccd20`](#insn-004ccd20)

~~~json
{
  "source": "004ccd20",
  "target": "004ccd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccd28`](#insn-004ccd28)

~~~json
{
  "source": "004ccd28",
  "target": "0054052c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ccd2c`](#insn-004ccd2c)

~~~json
{
  "source": "004ccd2c",
  "target": "004ccd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccd30`](#insn-004ccd30)

~~~json
{
  "source": "004ccd30",
  "target": "004ccd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccd5c`](#insn-004ccd5c)

~~~json
{
  "source": "004ccd5c",
  "target": "004ccd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccd64`](#insn-004ccd64)

~~~json
{
  "source": "004ccd64",
  "target": "0054052c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ccd68`](#insn-004ccd68)

~~~json
{
  "source": "004ccd68",
  "target": "004ccd78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccd6c`](#insn-004ccd6c)

~~~json
{
  "source": "004ccd6c",
  "target": "004ccd78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccd84`](#insn-004ccd84)

~~~json
{
  "source": "004ccd84",
  "target": "004ccd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccd8c`](#insn-004ccd8c)

~~~json
{
  "source": "004ccd8c",
  "target": "00c58160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ccd9c`](#insn-004ccd9c)

~~~json
{
  "source": "004ccd9c",
  "target": "004ccda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccda4`](#insn-004ccda4)

~~~json
{
  "source": "004ccda4",
  "target": "00c58160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ccdbc`](#insn-004ccdbc)

~~~json
{
  "source": "004ccdbc",
  "target": "004ccf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccdf4`](#insn-004ccdf4)

~~~json
{
  "source": "004ccdf4",
  "target": "004b3548",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ccdfc`](#insn-004ccdfc)

~~~json
{
  "source": "004ccdfc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cce0c`](#insn-004cce0c)

~~~json
{
  "source": "004cce0c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cce1c`](#insn-004cce1c)

~~~json
{
  "source": "004cce1c",
  "target": "004cce3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cce38`](#insn-004cce38)

~~~json
{
  "source": "004cce38",
  "target": "004cce20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cce3c`](#insn-004cce3c)

~~~json
{
  "source": "004cce3c",
  "target": "004cce84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cce44`](#insn-004cce44)

~~~json
{
  "source": "004cce44",
  "target": "004cce60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cce50`](#insn-004cce50)

~~~json
{
  "source": "004cce50",
  "target": "004cd0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cce5c`](#insn-004cce5c)

~~~json
{
  "source": "004cce5c",
  "target": "004cd0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cce80`](#insn-004cce80)

~~~json
{
  "source": "004cce80",
  "target": "004cce6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cce84`](#insn-004cce84)

~~~json
{
  "source": "004cce84",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cce94`](#insn-004cce94)

~~~json
{
  "source": "004cce94",
  "target": "004cceb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cceb0`](#insn-004cceb0)

~~~json
{
  "source": "004cceb0",
  "target": "004cce98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cceb4`](#insn-004cceb4)

~~~json
{
  "source": "004cceb4",
  "target": "004ccefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccebc`](#insn-004ccebc)

~~~json
{
  "source": "004ccebc",
  "target": "004cced8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccec8`](#insn-004ccec8)

~~~json
{
  "source": "004ccec8",
  "target": "004cd114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cced4`](#insn-004cced4)

~~~json
{
  "source": "004cced4",
  "target": "004cd114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccef8`](#insn-004ccef8)

~~~json
{
  "source": "004ccef8",
  "target": "004ccee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccefc`](#insn-004ccefc)

~~~json
{
  "source": "004ccefc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccf00`](#insn-004ccf00)

~~~json
{
  "source": "004ccf00",
  "target": "004cd028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccf04`](#insn-004ccf04)

~~~json
{
  "source": "004ccf04",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccf08`](#insn-004ccf08)

~~~json
{
  "source": "004ccf08",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccf10`](#insn-004ccf10)

~~~json
{
  "source": "004ccf10",
  "target": "00c67808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67808",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ccf20`](#insn-004ccf20)

~~~json
{
  "source": "004ccf20",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ccf28`](#insn-004ccf28)

~~~json
{
  "source": "004ccf28",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ccf2c`](#insn-004ccf2c)

~~~json
{
  "source": "004ccf2c",
  "target": "004cd028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccf38`](#insn-004ccf38)

~~~json
{
  "source": "004ccf38",
  "target": "004ccf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccf5c`](#insn-004ccf5c)

~~~json
{
  "source": "004ccf5c",
  "target": "004ccf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccf60`](#insn-004ccf60)

~~~json
{
  "source": "004ccf60",
  "target": "004ccf74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccf64`](#insn-004ccf64)

~~~json
{
  "source": "004ccf64",
  "target": "004ccfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccf70`](#insn-004ccf70)

~~~json
{
  "source": "004ccf70",
  "target": "004ccfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccf78`](#insn-004ccf78)

~~~json
{
  "source": "004ccf78",
  "target": "004ccf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccf84`](#insn-004ccf84)

~~~json
{
  "source": "004ccf84",
  "target": "004cd06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccf90`](#insn-004ccf90)

~~~json
{
  "source": "004ccf90",
  "target": "004cd06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccfb4`](#insn-004ccfb4)

~~~json
{
  "source": "004ccfb4",
  "target": "004ccfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccfc0`](#insn-004ccfc0)

~~~json
{
  "source": "004ccfc0",
  "target": "004ccfe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccfdc`](#insn-004ccfdc)

~~~json
{
  "source": "004ccfdc",
  "target": "004ccfc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccfe0`](#insn-004ccfe0)

~~~json
{
  "source": "004ccfe0",
  "target": "004cd028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccfe8`](#insn-004ccfe8)

~~~json
{
  "source": "004ccfe8",
  "target": "004cd004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccff4`](#insn-004ccff4)

~~~json
{
  "source": "004ccff4",
  "target": "004cd0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd000`](#insn-004cd000)

~~~json
{
  "source": "004cd000",
  "target": "004cd0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd024`](#insn-004cd024)

~~~json
{
  "source": "004cd024",
  "target": "004cd010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd044`](#insn-004cd044)

~~~json
{
  "source": "004cd044",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd04c`](#insn-004cd04c)

~~~json
{
  "source": "004cd04c",
  "target": "004cd174",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd050`](#insn-004cd050)

~~~json
{
  "source": "004cd050",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd054`](#insn-004cd054)

~~~json
{
  "source": "004cd054",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd058`](#insn-004cd058)

~~~json
{
  "source": "004cd058",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd05c`](#insn-004cd05c)

~~~json
{
  "source": "004cd05c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd060`](#insn-004cd060)

~~~json
{
  "source": "004cd060",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd094`](#insn-004cd094)

~~~json
{
  "source": "004cd094",
  "target": "004cd080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd09c`](#insn-004cd09c)

~~~json
{
  "source": "004cd09c",
  "target": "004ccfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd0a0`](#insn-004cd0a0)

~~~json
{
  "source": "004cd0a0",
  "target": "004ccfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd0cc`](#insn-004cd0cc)

~~~json
{
  "source": "004cd0cc",
  "target": "004cd0b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd0d4`](#insn-004cd0d4)

~~~json
{
  "source": "004cd0d4",
  "target": "004cd010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd0d8`](#insn-004cd0d8)

~~~json
{
  "source": "004cd0d8",
  "target": "004cd028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd104`](#insn-004cd104)

~~~json
{
  "source": "004cd104",
  "target": "004cd0f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd10c`](#insn-004cd10c)

~~~json
{
  "source": "004cd10c",
  "target": "004cce6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd110`](#insn-004cd110)

~~~json
{
  "source": "004cd110",
  "target": "004cce84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd13c`](#insn-004cd13c)

~~~json
{
  "source": "004cd13c",
  "target": "004cd128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd144`](#insn-004cd144)

~~~json
{
  "source": "004cd144",
  "target": "004ccee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd148`](#insn-004cd148)

~~~json
{
  "source": "004cd148",
  "target": "004ccefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cd174`](#insn-004cd174)

~~~json
{
  "source": "004cd174",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
