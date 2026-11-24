# 004bcccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00499e34`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499e34.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0007.md#compare-2018d8d7edeecfdd42c9777035fd49c6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `004bcd0c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcd0c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0008.md#compare-87d99852b4fdee8f76fd8092777b7ebe)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004bcccc",
  "name": "_ZN5Botan14CBC_Encryption7processEPhm",
  "size": 620,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b2b3f94ea0d7801b97ff70eb8e722656efc3c996e96729d746a240d90f6f4ae7",
  "source_text_sha256": "b2b3f94ea0d7801b97ff70eb8e722656efc3c996e96729d746a240d90f6f4ae7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004bcccc",
        "004bcf37"
      ]
    ],
    "bytes_sha256": "d60c7a7e27fdbe108429d8dd1000f5d75b25bcd639c94357a823c2a221086724",
    "instruction_count": 155,
    "instruction_bytes": 620,
    "body_bytes": 620,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00543818](../00543/00543818.md)
- [00c58250](../00c58/00c58250.md)

## 関連文字列（未確認候補）

~~~text
"/Users/battlecats/.jenkins/workspace/Battlecats-Jp-Android/release_jp-android-16.0.0/Source/android_cpp/app/src/main/cpp/botan/botan_all.cpp"
"CBC input is full blocks"
"process"
"sz % BS == 0"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 12270 bytes

~~~c

ulong _ZN5Botan14CBC_Encryption7processEPhm(long param_1,byte *param_2,ulong param_3)

{
  ulong uVar1;
  bool bVar2;
  byte *pbVar3;
  byte *pbVar4;
  byte *pbVar5;
  ulong uVar6;
  byte *pbVar7;
  byte *pbVar8;
  ulong uVar9;
  ulong uVar10;
  ulong uVar11;
  ulong uVar12;
  undefined8 uVar13;
  undefined8 uVar14;
  undefined8 uVar15;
  undefined8 uVar16;
  
  pbVar4 = *(byte **)(param_1 + 0x18);
  uVar11 = *(long *)(param_1 + 0x20) - (long)pbVar4;
  uVar1 = 0;
  if (uVar11 != 0) {
    uVar1 = param_3 / uVar11;
  }
  if (param_3 != uVar1 * uVar11) {
                    /* WARNING: Subroutine does not return */
    _ZN5Botan17assertion_failureEPKcS1_S1_S1_i
              ("sz % BS == 0","CBC input is full blocks","process",
               "/Users/battlecats/.jenkins/workspace/Battlecats-Jp-Android/release_jp-android-16.0.0/Source/android_cpp/app/src/main/cpp/botan/botan_all.cpp"
               ,0x14d2);
  }
  uVar12 = uVar11;
  pbVar7 = param_2;
  if (param_3 < uVar11) {
    return param_3;
  }
  for (; 0xf < uVar12; uVar12 = uVar12 - 0x10) {
    uVar15 = *(undefined8 *)(pbVar4 + 8);
    uVar13 = *(undefined8 *)pbVar4;
    uVar16 = *(undefined8 *)(pbVar7 + 8);
    uVar14 = *(undefined8 *)pbVar7;
    *(ulong *)(pbVar7 + 8) =
         CONCAT17((byte)((ulong)uVar16 >> 0x38) ^ (byte)((ulong)uVar15 >> 0x38),
                  CONCAT16((byte)((ulong)uVar16 >> 0x30) ^ (byte)((ulong)uVar15 >> 0x30),
                           CONCAT15((byte)((ulong)uVar16 >> 0x28) ^ (byte)((ulong)uVar15 >> 0x28),
                                    CONCAT14((byte)((ulong)uVar16 >> 0x20) ^
                                             (byte)((ulong)uVar15 >> 0x20),
                                             CONCAT13((byte)((ulong)uVar16 >> 0x18) ^
                                                      (byte)((ulong)uVar15 >> 0x18),
                                                      CONCAT12((byte)((ulong)uVar16 >> 0x10) ^
                                                               (byte)((ulong)uVar15 >> 0x10),
                                                               CONCAT11((byte)((ulong)uVar16 >> 8) ^
                                                                        (byte)((ulong)uVar15 >> 8),
                                                                        (byte)uVar16 ^ (byte)uVar15)
                                                              ))))));
    *(ulong *)pbVar7 =
         CONCAT17((byte)((ulong)uVar14 >> 0x38) ^ (byte)((ulong)uVar13 >> 0x38),
                  CONCAT16((byte)((ulong)uVar14 >> 0x30) ^ (byte)((ulong)uVar13 >> 0x30),
                           CONCAT15((byte)((ulong)uVar14 >> 0x28) ^ (byte)((ulong)uVar13 >> 0x28),
                                    CONCAT14((byte)((ulong)uVar14 >> 0x20) ^
                                             (byte)((ulong)uVar13 >> 0x20),
                                             CONCAT13((byte)((ulong)uVar14 >> 0x18) ^
                                                      (byte)((ulong)uVar13 >> 0x18),
                                                      CONCAT12((byte)((ulong)uVar14 >> 0x10) ^
                                                               (byte)((ulong)uVar13 >> 0x10),
                                                               CONCAT11((byte)((ulong)uVar14 >> 8) ^
                                                                        (byte)((ulong)uVar13 >> 8),
                                                                        (byte)uVar14 ^ (byte)uVar13)
                                                              ))))));
    pbVar4 = pbVar4 + 0x10;
    pbVar7 = pbVar7 + 0x10;
  }
  if (uVar12 != 0) {
    if ((7 < uVar12) && ((pbVar4 + uVar12 <= pbVar7 || (pbVar7 + uVar12 <= pbVar4)))) {
      uVar10 = uVar12 & 8;
      pbVar3 = pbVar4;
      pbVar5 = pbVar7;
      uVar6 = uVar10;
      do {
        uVar13 = *(undefined8 *)pbVar3;
        uVar15 = *(undefined8 *)pbVar5;
        uVar6 = uVar6 - 8;
        *(ulong *)pbVar5 =
             CONCAT17((byte)((ulong)uVar15 >> 0x38) ^ (byte)((ulong)uVar13 >> 0x38),
                      CONCAT16((byte)((ulong)uVar15 >> 0x30) ^ (byte)((ulong)uVar13 >> 0x30),
                               CONCAT15((byte)((ulong)uVar15 >> 0x28) ^
                                        (byte)((ulong)uVar13 >> 0x28),
                                        CONCAT14((byte)((ulong)uVar15 >> 0x20) ^
                                                 (byte)((ulong)uVar13 >> 0x20),
                                                 CONCAT13((byte)((ulong)uVar15 >> 0x18) ^
                                                          (byte)((ulong)uVar13 >> 0x18),
                                                          CONCAT12((byte)((ulong)uVar15 >> 0x10) ^
                                                                   (byte)((ulong)uVar13 >> 0x10),
                                                                   CONCAT11((byte)((ulong)uVar15 >>
                                                                                  8) ^
                                                                            (byte)((ulong)uVar13 >>
                                                                                  8),(byte)uVar15 ^
                                                                                     (byte)uVar13)))
                                                ))));
        pbVar3 = pbVar3 + 8;
        pbVar5 = pbVar5 + 8;
      } while (uVar6 != 0);
      bVar2 = uVar12 == uVar10;
      uVar12 = uVar12 & 7;
      pbVar4 = pbVar4 + uVar10;
      pbVar7 = pbVar7 + uVar10;
      if (bVar2) goto LAB_004bcd94;
    }
    do {
      uVar12 = uVar12 - 1;
      *pbVar7 = *pbVar7 ^ *pbVar4;
      pbVar4 = pbVar4 + 1;
      pbVar7 = pbVar7 + 1;
    } while (uVar12 != 0);
  }
LAB_004bcd94:
  (**(code **)(**(long **)(param_1 + 8) + 0x48))(*(long **)(param_1 + 8),param_2,param_2,1);
  if (uVar1 - 1 != 0) {
    uVar12 = 1;
    do {
      pbVar3 = param_2 + uVar12 * uVar11;
      pbVar4 = param_2 + (uVar12 - 1) * uVar11;
      uVar6 = uVar11;
      pbVar7 = pbVar3;
      if (0xf < uVar11) {
        do {
          uVar15 = *(undefined8 *)(pbVar4 + 8);
          uVar13 = *(undefined8 *)pbVar4;
          uVar16 = *(undefined8 *)(pbVar4 + uVar11 + 8);
          uVar14 = *(undefined8 *)(pbVar4 + uVar11);
          uVar6 = uVar6 - 0x10;
          *(ulong *)(pbVar4 + uVar11 + 8) =
               CONCAT17((byte)((ulong)uVar16 >> 0x38) ^ (byte)((ulong)uVar15 >> 0x38),
                        CONCAT16((byte)((ulong)uVar16 >> 0x30) ^ (byte)((ulong)uVar15 >> 0x30),
                                 CONCAT15((byte)((ulong)uVar16 >> 0x28) ^
                                          (byte)((ulong)uVar15 >> 0x28),
                                          CONCAT14((byte)((ulong)uVar16 >> 0x20) ^
                                                   (byte)((ulong)uVar15 >> 0x20),
                                                   CONCAT13((byte)((ulong)uVar16 >> 0x18) ^
                                                            (byte)((ulong)uVar15 >> 0x18),
                                                            CONCAT12((byte)((ulong)uVar16 >> 0x10) ^
                                                                     (byte)((ulong)uVar15 >> 0x10),
                                                                     CONCAT11((byte)((ulong)uVar16
                                                                                    >> 8) ^
                                                                              (byte)((ulong)uVar15
                                                                                    >> 8),
                                                                              (byte)uVar16 ^
                                                                              (byte)uVar15)))))));
          *(ulong *)(pbVar4 + uVar11) =
               CONCAT17((byte)((ulong)uVar14 >> 0x38) ^ (byte)((ulong)uVar13 >> 0x38),
                        CONCAT16((byte)((ulong)uVar14 >> 0x30) ^ (byte)((ulong)uVar13 >> 0x30),
                                 CONCAT15((byte)((ulong)uVar14 >> 0x28) ^
                                          (byte)((ulong)uVar13 >> 0x28),
                                          CONCAT14((byte)((ulong)uVar14 >> 0x20) ^
                                                   (byte)((ulong)uVar13 >> 0x20),
                                                   CONCAT13((byte)((ulong)uVar14 >> 0x18) ^
                                                            (byte)((ulong)uVar13 >> 0x18),
                                                            CONCAT12((byte)((ulong)uVar14 >> 0x10) ^
                                                                     (byte)((ulong)uVar13 >> 0x10),
                                                                     CONCAT11((byte)((ulong)uVar14
                                                                                    >> 8) ^
                                                                              (byte)((ulong)uVar13
                                                                                    >> 8),
                                                                              (byte)uVar14 ^
                                                                              (byte)uVar13)))))));
          pbVar4 = pbVar4 + 0x10;
        } while (0xf < uVar6);
        pbVar7 = pbVar4 + uVar11;
      }
      if (uVar6 != 0) {
        if ((7 < uVar6) && ((pbVar4 + uVar6 <= pbVar7 || (pbVar7 + uVar6 <= pbVar4)))) {
          uVar9 = uVar6 & 8;
          pbVar5 = pbVar4;
          pbVar8 = pbVar7;
          uVar10 = uVar9;
          do {
            uVar13 = *(undefined8 *)pbVar5;
            uVar15 = *(undefined8 *)pbVar8;
            uVar10 = uVar10 - 8;
            *(ulong *)pbVar8 =
                 CONCAT17((byte)((ulong)uVar15 >> 0x38) ^ (byte)((ulong)uVar13 >> 0x38),
                          CONCAT16((byte)((ulong)uVar15 >> 0x30) ^ (byte)((ulong)uVar13 >> 0x30),
                                   CONCAT15((byte)((ulong)uVar15 >> 0x28) ^
                                            (byte)((ulong)uVar13 >> 0x28),
                                            CONCAT14((byte)((ulong)uVar15 >> 0x20) ^
                                                     (byte)((ulong)uVar13 >> 0x20),
                                                     CONCAT13((byte)((ulong)uVar15 >> 0x18) ^
                                                              (byte)((ulong)uVar13 >> 0x18),
                                                              CONCAT12((byte)((ulong)uVar15 >> 0x10)
                                                                       ^ (byte)((ulong)uVar13 >>
                                                                               0x10),
                                                                       CONCAT11((byte)((ulong)uVar15
                                                                                      >> 8) ^
                                                                                (byte)((ulong)uVar13
                                                                                      >> 8),
                                                                                (byte)uVar15 ^
                                                                                (byte)uVar13)))))));
            pbVar5 = pbVar5 + 8;
            pbVar8 = pbVar8 + 8;
          } while (uVar10 != 0);
          bVar2 = uVar6 == uVar9;
          uVar6 = uVar6 & 7;
          pbVar4 = pbVar4 + uVar9;
          pbVar7 = pbVar7 + uVar9;
          if (bVar2) goto LAB_004bcdf0;
        }
        do {
          uVar6 = uVar6 - 1;
          *pbVar7 = *pbVar7 ^ *pbVar4;
          pbVar4 = pbVar4 + 1;
          pbVar7 = pbVar7 + 1;
        } while (uVar6 != 0);
      }
LAB_004bcdf0:
      (**(code **)(**(long **)(param_1 + 8) + 0x48))(*(long **)(param_1 + 8),pbVar3,pbVar3,1);
      uVar12 = uVar12 + 1;
    } while (uVar12 != uVar1);
  }
  FUN_00543818((undefined8 *)(param_1 + 0x18),param_2 + (uVar1 - 1) * uVar11,
               param_2 + uVar1 * uVar11,
               (long)(param_2 + uVar1 * uVar11) - (long)(param_2 + (uVar1 - 1) * uVar11));
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004bcccc"></a> `004bcccc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-004bccd0"></a> `004bccd0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004bccd4"></a> `004bccd4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004bccd8"></a> `004bccd8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bccdc"></a> `004bccdc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bcce0"></a> `004bcce0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-004bcce4"></a> `004bcce4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004bcce8"></a> `004bcce8` | `88 a6 c1 a9` | ldp x8,x9,[x20, #0x18]! | `FALL_THROUGH`
<a id="insn-004bccec"></a> `004bccec` | `37 01 08 cb` | sub x23,x9,x8 | `FALL_THROUGH`
<a id="insn-004bccf0"></a> `004bccf0` | `58 08 d7 9a` | udiv x24,x2,x23 | `FALL_THROUGH`
<a id="insn-004bccf4"></a> `004bccf4` | `09 8b 17 9b` | msub x9,x24,x23,x2 | `FALL_THROUGH`
<a id="insn-004bccf8"></a> `004bccf8` | `c9 10 00 b5` | cbnz x9,0x004bcf10 | `CONDITIONAL_JUMP`
<a id="insn-004bccfc"></a> `004bccfc` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-004bcd00"></a> `004bcd00` | `ff 02 02 eb` | cmp x23,x2 | `FALL_THROUGH`
<a id="insn-004bcd04"></a> `004bcd04` | `48 06 00 54` | b.hi 0x004bcdcc | `CONDITIONAL_JUMP`
<a id="insn-004bcd08"></a> `004bcd08` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-004bcd0c"></a> `004bcd0c` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-004bcd10"></a> `004bcd10` | `ff 42 00 f1` | cmp x23,#0x10 | `FALL_THROUGH`
<a id="insn-004bcd14"></a> `004bcd14` | `83 01 00 54` | b.cc 0x004bcd44 | `CONDITIONAL_JUMP`
<a id="insn-004bcd18"></a> `004bcd18` | `ea 03 17 aa` | mov x10,x23 | `FALL_THROUGH`
<a id="insn-004bcd1c"></a> `004bcd1c` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-004bcd20"></a> `004bcd20` | `00 05 c1 3c` | ldr q0,[x8], #0x10 | `FALL_THROUGH`
<a id="insn-004bcd24"></a> `004bcd24` | `21 01 c0 3d` | ldr q1,[x9] | `FALL_THROUGH`
<a id="insn-004bcd28"></a> `004bcd28` | `4a 41 00 d1` | sub x10,x10,#0x10 | `FALL_THROUGH`
<a id="insn-004bcd2c"></a> `004bcd2c` | `20 1c 20 6e` | eor v0.16B,v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-004bcd30"></a> `004bcd30` | `5f 3d 00 f1` | cmp x10,#0xf | `FALL_THROUGH`
<a id="insn-004bcd34"></a> `004bcd34` | `20 05 81 3c` | str q0,[x9], #0x10 | `FALL_THROUGH`
<a id="insn-004bcd38"></a> `004bcd38` | `48 ff ff 54` | b.hi 0x004bcd20 | `CONDITIONAL_JUMP`
<a id="insn-004bcd3c"></a> `004bcd3c` | `aa 00 00 b5` | cbnz x10,0x004bcd50 | `CONDITIONAL_JUMP`
<a id="insn-004bcd40"></a> `004bcd40` | `15 00 00 14` | b 0x004bcd94 | `UNCONDITIONAL_JUMP`
<a id="insn-004bcd44"></a> `004bcd44` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-004bcd48"></a> `004bcd48` | `ea 03 17 aa` | mov x10,x23 | `FALL_THROUGH`
<a id="insn-004bcd4c"></a> `004bcd4c` | `4a 02 00 b4` | cbz x10,0x004bcd94 | `CONDITIONAL_JUMP`
<a id="insn-004bcd50"></a> `004bcd50` | `5f 21 00 f1` | cmp x10,#0x8 | `FALL_THROUGH`
<a id="insn-004bcd54"></a> `004bcd54` | `e3 00 00 54` | b.cc 0x004bcd70 | `CONDITIONAL_JUMP`
<a id="insn-004bcd58"></a> `004bcd58` | `0b 01 0a 8b` | add x11,x8,x10 | `FALL_THROUGH`
<a id="insn-004bcd5c"></a> `004bcd5c` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-004bcd60"></a> `004bcd60` | `c2 0b 00 54` | b.cs 0x004bced8 | `CONDITIONAL_JUMP`
<a id="insn-004bcd64"></a> `004bcd64` | `2b 01 0a 8b` | add x11,x9,x10 | `FALL_THROUGH`
<a id="insn-004bcd68"></a> `004bcd68` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-004bcd6c"></a> `004bcd6c` | `62 0b 00 54` | b.cs 0x004bced8 | `CONDITIONAL_JUMP`
<a id="insn-004bcd70"></a> `004bcd70` | `eb 03 0a aa` | mov x11,x10 | `FALL_THROUGH`
<a id="insn-004bcd74"></a> `004bcd74` | `ec 03 08 aa` | mov x12,x8 | `FALL_THROUGH`
<a id="insn-004bcd78"></a> `004bcd78` | `ed 03 09 aa` | mov x13,x9 | `FALL_THROUGH`
<a id="insn-004bcd7c"></a> `004bcd7c` | `88 15 40 38` | ldrb w8,[x12], #0x1 | `FALL_THROUGH`
<a id="insn-004bcd80"></a> `004bcd80` | `a9 01 40 39` | ldrb w9,[x13] | `FALL_THROUGH`
<a id="insn-004bcd84"></a> `004bcd84` | `6b 05 00 f1` | subs x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-004bcd88"></a> `004bcd88` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-004bcd8c"></a> `004bcd8c` | `a8 15 00 38` | strb w8,[x13], #0x1 | `FALL_THROUGH`
<a id="insn-004bcd90"></a> `004bcd90` | `61 ff ff 54` | b.ne 0x004bcd7c | `CONDITIONAL_JUMP`
<a id="insn-004bcd94"></a> `004bcd94` | `a0 06 40 f9` | ldr x0,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-004bcd98"></a> `004bcd98` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-004bcd9c"></a> `004bcd9c` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-004bcda0"></a> `004bcda0` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-004bcda4"></a> `004bcda4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004bcda8"></a> `004bcda8` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-004bcdac"></a> `004bcdac` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004bcdb0"></a> `004bcdb0` | `19 07 00 f1` | subs x25,x24,#0x1 | `FALL_THROUGH`
<a id="insn-004bcdb4"></a> `004bcdb4` | `a1 01 00 54` | b.ne 0x004bcde8 | `CONDITIONAL_JUMP`
<a id="insn-004bcdb8"></a> `004bcdb8` | `21 5b 17 9b` | madd x1,x25,x23,x22 | `FALL_THROUGH`
<a id="insn-004bcdbc"></a> `004bcdbc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004bcdc0"></a> `004bcdc0` | `02 5b 17 9b` | madd x2,x24,x23,x22 | `FALL_THROUGH`
<a id="insn-004bcdc4"></a> `004bcdc4` | `43 00 01 cb` | sub x3,x2,x1 | `FALL_THROUGH`
<a id="insn-004bcdc8"></a> `004bcdc8` | `94 1a 02 94` | bl 0x00543818 | `UNCONDITIONAL_CALL`
<a id="insn-004bcdcc"></a> `004bcdcc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bcdd0"></a> `004bcdd0` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bcdd4"></a> `004bcdd4` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bcdd8"></a> `004bcdd8` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004bcddc"></a> `004bcddc` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004bcde0"></a> `004bcde0` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-004bcde4"></a> `004bcde4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004bcde8"></a> `004bcde8` | `3a 00 80 52` | mov w26,#0x1 | `FALL_THROUGH`
<a id="insn-004bcdec"></a> `004bcdec` | `0a 00 00 14` | b 0x004bce14 | `UNCONDITIONAL_JUMP`
<a id="insn-004bcdf0"></a> `004bcdf0` | `a0 06 40 f9` | ldr x0,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-004bcdf4"></a> `004bcdf4` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-004bcdf8"></a> `004bcdf8` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-004bcdfc"></a> `004bcdfc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004bce00"></a> `004bce00` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-004bce04"></a> `004bce04` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004bce08"></a> `004bce08` | `5a 07 00 91` | add x26,x26,#0x1 | `FALL_THROUGH`
<a id="insn-004bce0c"></a> `004bce0c` | `5f 03 18 eb` | cmp x26,x24 | `FALL_THROUGH`
<a id="insn-004bce10"></a> `004bce10` | `40 fd ff 54` | b.eq 0x004bcdb8 | `CONDITIONAL_JUMP`
<a id="insn-004bce14"></a> `004bce14` | `41 5b 17 9b` | madd x1,x26,x23,x22 | `FALL_THROUGH`
<a id="insn-004bce18"></a> `004bce18` | `48 07 00 d1` | sub x8,x26,#0x1 | `FALL_THROUGH`
<a id="insn-004bce1c"></a> `004bce1c` | `ff 42 00 f1` | cmp x23,#0x10 | `FALL_THROUGH`
<a id="insn-004bce20"></a> `004bce20` | `e9 03 17 aa` | mov x9,x23 | `FALL_THROUGH`
<a id="insn-004bce24"></a> `004bce24` | `08 59 17 9b` | madd x8,x8,x23,x22 | `FALL_THROUGH`
<a id="insn-004bce28"></a> `004bce28` | `eb 03 01 aa` | mov x11,x1 | `FALL_THROUGH`
<a id="insn-004bce2c"></a> `004bce2c` | `43 01 00 54` | b.cc 0x004bce54 | `CONDITIONAL_JUMP`
<a id="insn-004bce30"></a> `004bce30` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-004bce34"></a> `004bce34` | `01 69 f7 3c` | ldr q1,[x8,x23] | `FALL_THROUGH`
<a id="insn-004bce38"></a> `004bce38` | `29 41 00 d1` | sub x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-004bce3c"></a> `004bce3c` | `3f 3d 00 f1` | cmp x9,#0xf | `FALL_THROUGH`
<a id="insn-004bce40"></a> `004bce40` | `20 1c 20 6e` | eor v0.16B,v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-004bce44"></a> `004bce44` | `00 69 b7 3c` | str q0,[x8,x23] | `FALL_THROUGH`
<a id="insn-004bce48"></a> `004bce48` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004bce4c"></a> `004bce4c` | `28 ff ff 54` | b.hi 0x004bce30 | `CONDITIONAL_JUMP`
<a id="insn-004bce50"></a> `004bce50` | `0b 01 17 8b` | add x11,x8,x23 | `FALL_THROUGH`
<a id="insn-004bce54"></a> `004bce54` | `e9 fc ff b4` | cbz x9,0x004bcdf0 | `CONDITIONAL_JUMP`
<a id="insn-004bce58"></a> `004bce58` | `3f 21 00 f1` | cmp x9,#0x8 | `FALL_THROUGH`
<a id="insn-004bce5c"></a> `004bce5c` | `e3 00 00 54` | b.cc 0x004bce78 | `CONDITIONAL_JUMP`
<a id="insn-004bce60"></a> `004bce60` | `0a 01 09 8b` | add x10,x8,x9 | `FALL_THROUGH`
<a id="insn-004bce64"></a> `004bce64` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-004bce68"></a> `004bce68` | `c2 01 00 54` | b.cs 0x004bcea0 | `CONDITIONAL_JUMP`
<a id="insn-004bce6c"></a> `004bce6c` | `6a 01 09 8b` | add x10,x11,x9 | `FALL_THROUGH`
<a id="insn-004bce70"></a> `004bce70` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-004bce74"></a> `004bce74` | `62 01 00 54` | b.cs 0x004bcea0 | `CONDITIONAL_JUMP`
<a id="insn-004bce78"></a> `004bce78` | `ea 03 09 aa` | mov x10,x9 | `FALL_THROUGH`
<a id="insn-004bce7c"></a> `004bce7c` | `ec 03 08 aa` | mov x12,x8 | `FALL_THROUGH`
<a id="insn-004bce80"></a> `004bce80` | `ed 03 0b aa` | mov x13,x11 | `FALL_THROUGH`
<a id="insn-004bce84"></a> `004bce84` | `88 15 40 38` | ldrb w8,[x12], #0x1 | `FALL_THROUGH`
<a id="insn-004bce88"></a> `004bce88` | `a9 01 40 39` | ldrb w9,[x13] | `FALL_THROUGH`
<a id="insn-004bce8c"></a> `004bce8c` | `4a 05 00 f1` | subs x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-004bce90"></a> `004bce90` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-004bce94"></a> `004bce94` | `a8 15 00 38` | strb w8,[x13], #0x1 | `FALL_THROUGH`
<a id="insn-004bce98"></a> `004bce98` | `61 ff ff 54` | b.ne 0x004bce84 | `CONDITIONAL_JUMP`
<a id="insn-004bce9c"></a> `004bce9c` | `d5 ff ff 17` | b 0x004bcdf0 | `UNCONDITIONAL_JUMP`
<a id="insn-004bcea0"></a> `004bcea0` | `2e 01 7d 92` | and x14,x9,#0x8 | `FALL_THROUGH`
<a id="insn-004bcea4"></a> `004bcea4` | `2a 09 40 92` | and x10,x9,#0x7 | `FALL_THROUGH`
<a id="insn-004bcea8"></a> `004bcea8` | `0c 01 0e 8b` | add x12,x8,x14 | `FALL_THROUGH`
<a id="insn-004bceac"></a> `004bceac` | `6d 01 0e 8b` | add x13,x11,x14 | `FALL_THROUGH`
<a id="insn-004bceb0"></a> `004bceb0` | `ef 03 0e aa` | mov x15,x14 | `FALL_THROUGH`
<a id="insn-004bceb4"></a> `004bceb4` | `00 85 40 fc` | ldr d0,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-004bceb8"></a> `004bceb8` | `61 01 40 fd` | ldr d1,[x11] | `FALL_THROUGH`
<a id="insn-004bcebc"></a> `004bcebc` | `ef 21 00 f1` | subs x15,x15,#0x8 | `FALL_THROUGH`
<a id="insn-004bcec0"></a> `004bcec0` | `20 1c 20 2e` | eor v0.8B,v1.8B,v0.8B | `FALL_THROUGH`
<a id="insn-004bcec4"></a> `004bcec4` | `60 85 00 fc` | str d0,[x11], #0x8 | `FALL_THROUGH`
<a id="insn-004bcec8"></a> `004bcec8` | `61 ff ff 54` | b.ne 0x004bceb4 | `CONDITIONAL_JUMP`
<a id="insn-004bcecc"></a> `004bcecc` | `3f 01 0e eb` | cmp x9,x14 | `FALL_THROUGH`
<a id="insn-004bced0"></a> `004bced0` | `a1 fd ff 54` | b.ne 0x004bce84 | `CONDITIONAL_JUMP`
<a id="insn-004bced4"></a> `004bced4` | `c7 ff ff 17` | b 0x004bcdf0 | `UNCONDITIONAL_JUMP`
<a id="insn-004bced8"></a> `004bced8` | `4e 01 7d 92` | and x14,x10,#0x8 | `FALL_THROUGH`
<a id="insn-004bcedc"></a> `004bcedc` | `4b 09 40 92` | and x11,x10,#0x7 | `FALL_THROUGH`
<a id="insn-004bcee0"></a> `004bcee0` | `0c 01 0e 8b` | add x12,x8,x14 | `FALL_THROUGH`
<a id="insn-004bcee4"></a> `004bcee4` | `2d 01 0e 8b` | add x13,x9,x14 | `FALL_THROUGH`
<a id="insn-004bcee8"></a> `004bcee8` | `ef 03 0e aa` | mov x15,x14 | `FALL_THROUGH`
<a id="insn-004bceec"></a> `004bceec` | `00 85 40 fc` | ldr d0,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-004bcef0"></a> `004bcef0` | `21 01 40 fd` | ldr d1,[x9] | `FALL_THROUGH`
<a id="insn-004bcef4"></a> `004bcef4` | `ef 21 00 f1` | subs x15,x15,#0x8 | `FALL_THROUGH`
<a id="insn-004bcef8"></a> `004bcef8` | `20 1c 20 2e` | eor v0.8B,v1.8B,v0.8B | `FALL_THROUGH`
<a id="insn-004bcefc"></a> `004bcefc` | `20 85 00 fc` | str d0,[x9], #0x8 | `FALL_THROUGH`
<a id="insn-004bcf00"></a> `004bcf00` | `61 ff ff 54` | b.ne 0x004bceec | `CONDITIONAL_JUMP`
<a id="insn-004bcf04"></a> `004bcf04` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-004bcf08"></a> `004bcf08` | `a1 f3 ff 54` | b.ne 0x004bcd7c | `CONDITIONAL_JUMP`
<a id="insn-004bcf0c"></a> `004bcf0c` | `a2 ff ff 17` | b 0x004bcd94 | `UNCONDITIONAL_JUMP`
<a id="insn-004bcf10"></a> `004bcf10` | `60 ef ff 90` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-004bcf14"></a> `004bcf14` | `00 4c 2d 91` | add x0,x0,#0xb53 | `FALL_THROUGH`
<a id="insn-004bcf18"></a> `004bcf18` | `01 ef ff f0` | adrp x1,0x29f000 | `FALL_THROUGH`
<a id="insn-004bcf1c"></a> `004bcf1c` | `21 98 3d 91` | add x1,x1,#0xf66 | `FALL_THROUGH`
<a id="insn-004bcf20"></a> `004bcf20` | `42 ef ff 90` | adrp x2,0x2a4000 | `FALL_THROUGH`
<a id="insn-004bcf24"></a> `004bcf24` | `42 4c 01 91` | add x2,x2,#0x53 | `FALL_THROUGH`
<a id="insn-004bcf28"></a> `004bcf28` | `63 ef ff f0` | adrp x3,0x2ab000 | `FALL_THROUGH`
<a id="insn-004bcf2c"></a> `004bcf2c` | `63 9c 09 91` | add x3,x3,#0x267 | `FALL_THROUGH`
<a id="insn-004bcf30"></a> `004bcf30` | `44 9a 82 52` | mov w4,#0x14d2 | `FALL_THROUGH`
<a id="insn-004bcf34"></a> `004bcf34` | `c7 6c 1e 94` | bl 0x00c58250 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004bcccc`](#insn-004bcccc) 範囲 `[['004bcccc', '004bccfb']]`
  - `CONDITIONAL_JUMP` [`004bccf8`](#insn-004bccf8) → [`004bcf10`](#insn-004bcf10)
  - `FALL_THROUGH` [`004bccf8`](#insn-004bccf8) → [`004bccfc`](#insn-004bccfc)
- ブロック [`004bccfc`](#insn-004bccfc) 範囲 `[['004bccfc', '004bcd07']]`
  - `CONDITIONAL_JUMP` [`004bcd04`](#insn-004bcd04) → [`004bcdcc`](#insn-004bcdcc)
  - `FALL_THROUGH` [`004bcd04`](#insn-004bcd04) → [`004bcd08`](#insn-004bcd08)
- ブロック [`004bcd08`](#insn-004bcd08) 範囲 `[['004bcd08', '004bcd17']]`
  - `CONDITIONAL_JUMP` [`004bcd14`](#insn-004bcd14) → [`004bcd44`](#insn-004bcd44)
  - `FALL_THROUGH` [`004bcd14`](#insn-004bcd14) → [`004bcd18`](#insn-004bcd18)
- ブロック [`004bcd18`](#insn-004bcd18) 範囲 `[['004bcd18', '004bcd1f']]`
  - `FALL_THROUGH` [`004bcd1c`](#insn-004bcd1c) → [`004bcd20`](#insn-004bcd20)
- ブロック [`004bcd20`](#insn-004bcd20) 範囲 `[['004bcd20', '004bcd3b']]`
  - `CONDITIONAL_JUMP` [`004bcd38`](#insn-004bcd38) → [`004bcd20`](#insn-004bcd20)
  - `FALL_THROUGH` [`004bcd38`](#insn-004bcd38) → [`004bcd3c`](#insn-004bcd3c)
- ブロック [`004bcd3c`](#insn-004bcd3c) 範囲 `[['004bcd3c', '004bcd3f']]`
  - `CONDITIONAL_JUMP` [`004bcd3c`](#insn-004bcd3c) → [`004bcd50`](#insn-004bcd50)
  - `FALL_THROUGH` [`004bcd3c`](#insn-004bcd3c) → [`004bcd40`](#insn-004bcd40)
- ブロック [`004bcd40`](#insn-004bcd40) 範囲 `[['004bcd40', '004bcd43']]`
  - `UNCONDITIONAL_JUMP` [`004bcd40`](#insn-004bcd40) → [`004bcd94`](#insn-004bcd94)
- ブロック [`004bcd44`](#insn-004bcd44) 範囲 `[['004bcd44', '004bcd4f']]`
  - `CONDITIONAL_JUMP` [`004bcd4c`](#insn-004bcd4c) → [`004bcd94`](#insn-004bcd94)
  - `FALL_THROUGH` [`004bcd4c`](#insn-004bcd4c) → [`004bcd50`](#insn-004bcd50)
- ブロック [`004bcd50`](#insn-004bcd50) 範囲 `[['004bcd50', '004bcd57']]`
  - `CONDITIONAL_JUMP` [`004bcd54`](#insn-004bcd54) → [`004bcd70`](#insn-004bcd70)
  - `FALL_THROUGH` [`004bcd54`](#insn-004bcd54) → [`004bcd58`](#insn-004bcd58)
- ブロック [`004bcd58`](#insn-004bcd58) 範囲 `[['004bcd58', '004bcd63']]`
  - `CONDITIONAL_JUMP` [`004bcd60`](#insn-004bcd60) → [`004bced8`](#insn-004bced8)
  - `FALL_THROUGH` [`004bcd60`](#insn-004bcd60) → [`004bcd64`](#insn-004bcd64)
- ブロック [`004bcd64`](#insn-004bcd64) 範囲 `[['004bcd64', '004bcd6f']]`
  - `CONDITIONAL_JUMP` [`004bcd6c`](#insn-004bcd6c) → [`004bced8`](#insn-004bced8)
  - `FALL_THROUGH` [`004bcd6c`](#insn-004bcd6c) → [`004bcd70`](#insn-004bcd70)
- ブロック [`004bcd70`](#insn-004bcd70) 範囲 `[['004bcd70', '004bcd7b']]`
  - `FALL_THROUGH` [`004bcd78`](#insn-004bcd78) → [`004bcd7c`](#insn-004bcd7c)
- ブロック [`004bcd7c`](#insn-004bcd7c) 範囲 `[['004bcd7c', '004bcd93']]`
  - `CONDITIONAL_JUMP` [`004bcd90`](#insn-004bcd90) → [`004bcd7c`](#insn-004bcd7c)
  - `FALL_THROUGH` [`004bcd90`](#insn-004bcd90) → [`004bcd94`](#insn-004bcd94)
- ブロック [`004bcd94`](#insn-004bcd94) 範囲 `[['004bcd94', '004bcdb7']]`
  - `CONDITIONAL_JUMP` [`004bcdb4`](#insn-004bcdb4) → [`004bcde8`](#insn-004bcde8)
  - `FALL_THROUGH` [`004bcdb4`](#insn-004bcdb4) → [`004bcdb8`](#insn-004bcdb8)
- ブロック [`004bcdb8`](#insn-004bcdb8) 範囲 `[['004bcdb8', '004bcdcb']]`
  - `FALL_THROUGH` [`004bcdc8`](#insn-004bcdc8) → [`004bcdcc`](#insn-004bcdcc)
- ブロック [`004bcdcc`](#insn-004bcdcc) 範囲 `[['004bcdcc', '004bcde7']]`
- ブロック [`004bcde8`](#insn-004bcde8) 範囲 `[['004bcde8', '004bcdef']]`
  - `UNCONDITIONAL_JUMP` [`004bcdec`](#insn-004bcdec) → [`004bce14`](#insn-004bce14)
- ブロック [`004bcdf0`](#insn-004bcdf0) 範囲 `[['004bcdf0', '004bce13']]`
  - `CONDITIONAL_JUMP` [`004bce10`](#insn-004bce10) → [`004bcdb8`](#insn-004bcdb8)
  - `FALL_THROUGH` [`004bce10`](#insn-004bce10) → [`004bce14`](#insn-004bce14)
- ブロック [`004bce14`](#insn-004bce14) 範囲 `[['004bce14', '004bce2f']]`
  - `CONDITIONAL_JUMP` [`004bce2c`](#insn-004bce2c) → [`004bce54`](#insn-004bce54)
  - `FALL_THROUGH` [`004bce2c`](#insn-004bce2c) → [`004bce30`](#insn-004bce30)
- ブロック [`004bce30`](#insn-004bce30) 範囲 `[['004bce30', '004bce4f']]`
  - `CONDITIONAL_JUMP` [`004bce4c`](#insn-004bce4c) → [`004bce30`](#insn-004bce30)
  - `FALL_THROUGH` [`004bce4c`](#insn-004bce4c) → [`004bce50`](#insn-004bce50)
- ブロック [`004bce50`](#insn-004bce50) 範囲 `[['004bce50', '004bce53']]`
  - `FALL_THROUGH` [`004bce50`](#insn-004bce50) → [`004bce54`](#insn-004bce54)
- ブロック [`004bce54`](#insn-004bce54) 範囲 `[['004bce54', '004bce57']]`
  - `CONDITIONAL_JUMP` [`004bce54`](#insn-004bce54) → [`004bcdf0`](#insn-004bcdf0)
  - `FALL_THROUGH` [`004bce54`](#insn-004bce54) → [`004bce58`](#insn-004bce58)
- ブロック [`004bce58`](#insn-004bce58) 範囲 `[['004bce58', '004bce5f']]`
  - `CONDITIONAL_JUMP` [`004bce5c`](#insn-004bce5c) → [`004bce78`](#insn-004bce78)
  - `FALL_THROUGH` [`004bce5c`](#insn-004bce5c) → [`004bce60`](#insn-004bce60)
- ブロック [`004bce60`](#insn-004bce60) 範囲 `[['004bce60', '004bce6b']]`
  - `CONDITIONAL_JUMP` [`004bce68`](#insn-004bce68) → [`004bcea0`](#insn-004bcea0)
  - `FALL_THROUGH` [`004bce68`](#insn-004bce68) → [`004bce6c`](#insn-004bce6c)
- ブロック [`004bce6c`](#insn-004bce6c) 範囲 `[['004bce6c', '004bce77']]`
  - `CONDITIONAL_JUMP` [`004bce74`](#insn-004bce74) → [`004bcea0`](#insn-004bcea0)
  - `FALL_THROUGH` [`004bce74`](#insn-004bce74) → [`004bce78`](#insn-004bce78)
- ブロック [`004bce78`](#insn-004bce78) 範囲 `[['004bce78', '004bce83']]`
  - `FALL_THROUGH` [`004bce80`](#insn-004bce80) → [`004bce84`](#insn-004bce84)
- ブロック [`004bce84`](#insn-004bce84) 範囲 `[['004bce84', '004bce9b']]`
  - `CONDITIONAL_JUMP` [`004bce98`](#insn-004bce98) → [`004bce84`](#insn-004bce84)
  - `FALL_THROUGH` [`004bce98`](#insn-004bce98) → [`004bce9c`](#insn-004bce9c)
- ブロック [`004bce9c`](#insn-004bce9c) 範囲 `[['004bce9c', '004bce9f']]`
  - `UNCONDITIONAL_JUMP` [`004bce9c`](#insn-004bce9c) → [`004bcdf0`](#insn-004bcdf0)
- ブロック [`004bcea0`](#insn-004bcea0) 範囲 `[['004bcea0', '004bceb3']]`
  - `FALL_THROUGH` [`004bceb0`](#insn-004bceb0) → [`004bceb4`](#insn-004bceb4)
- ブロック [`004bceb4`](#insn-004bceb4) 範囲 `[['004bceb4', '004bcecb']]`
  - `CONDITIONAL_JUMP` [`004bcec8`](#insn-004bcec8) → [`004bceb4`](#insn-004bceb4)
  - `FALL_THROUGH` [`004bcec8`](#insn-004bcec8) → [`004bcecc`](#insn-004bcecc)
- ブロック [`004bcecc`](#insn-004bcecc) 範囲 `[['004bcecc', '004bced3']]`
  - `CONDITIONAL_JUMP` [`004bced0`](#insn-004bced0) → [`004bce84`](#insn-004bce84)
  - `FALL_THROUGH` [`004bced0`](#insn-004bced0) → [`004bced4`](#insn-004bced4)
- ブロック [`004bced4`](#insn-004bced4) 範囲 `[['004bced4', '004bced7']]`
  - `UNCONDITIONAL_JUMP` [`004bced4`](#insn-004bced4) → [`004bcdf0`](#insn-004bcdf0)
- ブロック [`004bced8`](#insn-004bced8) 範囲 `[['004bced8', '004bceeb']]`
  - `FALL_THROUGH` [`004bcee8`](#insn-004bcee8) → [`004bceec`](#insn-004bceec)
- ブロック [`004bceec`](#insn-004bceec) 範囲 `[['004bceec', '004bcf03']]`
  - `CONDITIONAL_JUMP` [`004bcf00`](#insn-004bcf00) → [`004bceec`](#insn-004bceec)
  - `FALL_THROUGH` [`004bcf00`](#insn-004bcf00) → [`004bcf04`](#insn-004bcf04)
- ブロック [`004bcf04`](#insn-004bcf04) 範囲 `[['004bcf04', '004bcf0b']]`
  - `CONDITIONAL_JUMP` [`004bcf08`](#insn-004bcf08) → [`004bcd7c`](#insn-004bcd7c)
  - `FALL_THROUGH` [`004bcf08`](#insn-004bcf08) → [`004bcf0c`](#insn-004bcf0c)
- ブロック [`004bcf0c`](#insn-004bcf0c) 範囲 `[['004bcf0c', '004bcf0f']]`
  - `UNCONDITIONAL_JUMP` [`004bcf0c`](#insn-004bcf0c) → [`004bcd94`](#insn-004bcd94)
- ブロック [`004bcf10`](#insn-004bcf10) 範囲 `[['004bcf10', '004bcf37']]`

## 命令位置別の参照

- [`004bcccc`](#insn-004bcccc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bccd0`](#insn-004bccd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bccd4`](#insn-004bccd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bccd8`](#insn-004bccd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bccdc`](#insn-004bccdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bccf8`](#insn-004bccf8) → [`004bcf10`](#insn-004bcf10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcd04`](#insn-004bcd04) → [`004bcdcc`](#insn-004bcdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcd14`](#insn-004bcd14) → [`004bcd44`](#insn-004bcd44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcd38`](#insn-004bcd38) → [`004bcd20`](#insn-004bcd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcd3c`](#insn-004bcd3c) → [`004bcd50`](#insn-004bcd50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcd40`](#insn-004bcd40) → [`004bcd94`](#insn-004bcd94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcd4c`](#insn-004bcd4c) → [`004bcd94`](#insn-004bcd94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcd54`](#insn-004bcd54) → [`004bcd70`](#insn-004bcd70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcd60`](#insn-004bcd60) → [`004bced8`](#insn-004bced8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcd6c`](#insn-004bcd6c) → [`004bced8`](#insn-004bced8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcd90`](#insn-004bcd90) → [`004bcd7c`](#insn-004bcd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcdb4`](#insn-004bcdb4) → [`004bcde8`](#insn-004bcde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcdc8`](#insn-004bcdc8) → [`00543818`](../00543/00543818.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00543818` · 推定シンボル `None` · 推定型 `None`
- [`004bcdd0`](#insn-004bcdd0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcdd4`](#insn-004bcdd4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcdd8`](#insn-004bcdd8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcddc`](#insn-004bcddc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcde0`](#insn-004bcde0) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcdec`](#insn-004bcdec) → [`004bce14`](#insn-004bce14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bce10`](#insn-004bce10) → [`004bcdb8`](#insn-004bcdb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bce2c`](#insn-004bce2c) → [`004bce54`](#insn-004bce54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bce4c`](#insn-004bce4c) → [`004bce30`](#insn-004bce30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bce54`](#insn-004bce54) → [`004bcdf0`](#insn-004bcdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bce5c`](#insn-004bce5c) → [`004bce78`](#insn-004bce78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bce68`](#insn-004bce68) → [`004bcea0`](#insn-004bcea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bce74`](#insn-004bce74) → [`004bcea0`](#insn-004bcea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bce98`](#insn-004bce98) → [`004bce84`](#insn-004bce84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bce9c`](#insn-004bce9c) → [`004bcdf0`](#insn-004bcdf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcec8`](#insn-004bcec8) → [`004bceb4`](#insn-004bceb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bced0`](#insn-004bced0) → [`004bce84`](#insn-004bce84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bced4`](#insn-004bced4) → [`004bcdf0`](#insn-004bcdf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcf00`](#insn-004bcf00) → [`004bceec`](#insn-004bceec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcf08`](#insn-004bcf08) → [`004bcd7c`](#insn-004bcd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcf0c`](#insn-004bcf0c) → [`004bcd94`](#insn-004bcd94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bcf14`](#insn-004bcf14) → `002a8b53`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bcf1c`](#insn-004bcf1c) → `0029ff66`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bcf24`](#insn-004bcf24) → `002a4053`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bcf2c`](#insn-004bcf2c) → `002ab267`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bcf34`](#insn-004bcf34) → [`00c58250`](../00c58/00c58250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58250` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004bcccc`](#insn-004bcccc)

~~~json
{
  "source": "004bcccc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bccd0`](#insn-004bccd0)

~~~json
{
  "source": "004bccd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bccd4`](#insn-004bccd4)

~~~json
{
  "source": "004bccd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bccd8`](#insn-004bccd8)

~~~json
{
  "source": "004bccd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bccdc`](#insn-004bccdc)

~~~json
{
  "source": "004bccdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bccf8`](#insn-004bccf8)

~~~json
{
  "source": "004bccf8",
  "target": "004bcf10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcd04`](#insn-004bcd04)

~~~json
{
  "source": "004bcd04",
  "target": "004bcdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcd14`](#insn-004bcd14)

~~~json
{
  "source": "004bcd14",
  "target": "004bcd44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcd38`](#insn-004bcd38)

~~~json
{
  "source": "004bcd38",
  "target": "004bcd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcd3c`](#insn-004bcd3c)

~~~json
{
  "source": "004bcd3c",
  "target": "004bcd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcd40`](#insn-004bcd40)

~~~json
{
  "source": "004bcd40",
  "target": "004bcd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcd4c`](#insn-004bcd4c)

~~~json
{
  "source": "004bcd4c",
  "target": "004bcd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcd54`](#insn-004bcd54)

~~~json
{
  "source": "004bcd54",
  "target": "004bcd70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcd60`](#insn-004bcd60)

~~~json
{
  "source": "004bcd60",
  "target": "004bced8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcd6c`](#insn-004bcd6c)

~~~json
{
  "source": "004bcd6c",
  "target": "004bced8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcd90`](#insn-004bcd90)

~~~json
{
  "source": "004bcd90",
  "target": "004bcd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcdb4`](#insn-004bcdb4)

~~~json
{
  "source": "004bcdb4",
  "target": "004bcde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcdc8`](#insn-004bcdc8)

~~~json
{
  "source": "004bcdc8",
  "target": "00543818",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bcdd0`](#insn-004bcdd0)

~~~json
{
  "source": "004bcdd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcdd4`](#insn-004bcdd4)

~~~json
{
  "source": "004bcdd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcdd8`](#insn-004bcdd8)

~~~json
{
  "source": "004bcdd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcddc`](#insn-004bcddc)

~~~json
{
  "source": "004bcddc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcde0`](#insn-004bcde0)

~~~json
{
  "source": "004bcde0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcdec`](#insn-004bcdec)

~~~json
{
  "source": "004bcdec",
  "target": "004bce14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bce10`](#insn-004bce10)

~~~json
{
  "source": "004bce10",
  "target": "004bcdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bce2c`](#insn-004bce2c)

~~~json
{
  "source": "004bce2c",
  "target": "004bce54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bce4c`](#insn-004bce4c)

~~~json
{
  "source": "004bce4c",
  "target": "004bce30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bce54`](#insn-004bce54)

~~~json
{
  "source": "004bce54",
  "target": "004bcdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bce5c`](#insn-004bce5c)

~~~json
{
  "source": "004bce5c",
  "target": "004bce78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bce68`](#insn-004bce68)

~~~json
{
  "source": "004bce68",
  "target": "004bcea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bce74`](#insn-004bce74)

~~~json
{
  "source": "004bce74",
  "target": "004bcea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bce98`](#insn-004bce98)

~~~json
{
  "source": "004bce98",
  "target": "004bce84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bce9c`](#insn-004bce9c)

~~~json
{
  "source": "004bce9c",
  "target": "004bcdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcec8`](#insn-004bcec8)

~~~json
{
  "source": "004bcec8",
  "target": "004bceb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bced0`](#insn-004bced0)

~~~json
{
  "source": "004bced0",
  "target": "004bce84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bced4`](#insn-004bced4)

~~~json
{
  "source": "004bced4",
  "target": "004bcdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcf00`](#insn-004bcf00)

~~~json
{
  "source": "004bcf00",
  "target": "004bceec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcf08`](#insn-004bcf08)

~~~json
{
  "source": "004bcf08",
  "target": "004bcd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcf0c`](#insn-004bcf0c)

~~~json
{
  "source": "004bcf0c",
  "target": "004bcd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bcf14`](#insn-004bcf14)

~~~json
{
  "source": "004bcf14",
  "target": "002a8b53",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8b53",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "737a2025204253203d3d203000",
  "capture_start": "002a8b53",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bcf1c`](#insn-004bcf1c)

~~~json
{
  "source": "004bcf1c",
  "target": "0029ff66",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ff66",
  "offset": 0,
  "size": 25,
  "datatype": "string",
  "bytes": "43424320696e7075742069732066756c6c20626c6f636b7300",
  "capture_start": "0029ff66",
  "capture_bytes": 25,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bcf24`](#insn-004bcf24)

~~~json
{
  "source": "004bcf24",
  "target": "002a4053",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4053",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "70726f6365737300",
  "capture_start": "002a4053",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bcf2c`](#insn-004bcf2c)

~~~json
{
  "source": "004bcf2c",
  "target": "002ab267",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ab267",
  "offset": 0,
  "size": 141,
  "datatype": "string",
  "bytes": "2f55736572732f626174746c65636174732f2e6a656e6b696e732f776f726b73",
  "capture_start": "002ab267",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`004bcf34`](#insn-004bcf34)

~~~json
{
  "source": "004bcf34",
  "target": "00c58250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
