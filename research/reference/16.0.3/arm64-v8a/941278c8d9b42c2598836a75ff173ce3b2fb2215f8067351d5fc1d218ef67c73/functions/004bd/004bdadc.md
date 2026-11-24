# 004bdadc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `004bd7bc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd7bc.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0008.md#compare-4848475102424115203c06f077fd3d15)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004bdadc",
  "name": "_ZN5Botan14CBC_Decryption7processEPhm",
  "size": 596,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "09c41675575ff3f413e10b865e0b2a0708c8165d71795ff962682a08eb9e6d01",
  "source_text_sha256": "09c41675575ff3f413e10b865e0b2a0708c8165d71795ff962682a08eb9e6d01",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004bdadc",
        "004bdd2f"
      ]
    ],
    "bytes_sha256": "e8bb62bfb69a78d20ab186aa1fb6e1cee4af030dfe755728d260bc2328eaa814",
    "instruction_count": 149,
    "instruction_bytes": 596,
    "body_bytes": 596,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58fe0](../00c58/00c58fe0.md)
- [00c596f0](../00c59/00c596f0.md)

## 関連文字列（未確認候補）

~~~text
"/Users/battlecats/.jenkins/workspace/Battlecats-Jp-Android/release_jp-android-16.0.3/Source/android_cpp/app/src/main/cpp/botan/botan_all.cpp"
"Input is full blocks"
"process"
"sz % BS == 0"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 12929 bytes

~~~c

ulong _ZN5Botan14CBC_Decryption7processEPhm(long param_1,byte *param_2,ulong param_3)

{
  ulong uVar1;
  bool bVar2;
  byte *pbVar3;
  ulong __n;
  byte *pbVar4;
  ulong uVar5;
  byte *pbVar6;
  byte *pbVar7;
  ulong uVar8;
  ulong uVar9;
  ulong __n_00;
  ulong uVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  undefined8 uVar14;
  
  __n_00 = *(long *)(param_1 + 0x20) - *(long *)(param_1 + 0x18);
  uVar10 = 0;
  if (__n_00 != 0) {
    uVar10 = param_3 / __n_00;
  }
  if (param_3 != uVar10 * __n_00) {
                    /* WARNING: Subroutine does not return */
    _ZN5Botan17assertion_failureEPKcS1_S1_S1_i
              ("sz % BS == 0","Input is full blocks","process",
               "/Users/battlecats/.jenkins/workspace/Battlecats-Jp-Android/release_jp-android-16.0.3/Source/android_cpp/app/src/main/cpp/botan/botan_all.cpp"
               ,0x153f);
  }
  if (__n_00 <= param_3) {
    do {
      __n = *(long *)(param_1 + 0x38) - *(long *)(param_1 + 0x30);
      if (uVar10 * __n_00 <= __n) {
        __n = uVar10 * __n_00;
      }
      uVar1 = 0;
      if (__n_00 != 0) {
        uVar1 = __n / __n_00;
      }
      (**(code **)(**(long **)(param_1 + 8) + 0x50))
                (*(long **)(param_1 + 8),param_2,*(long *)(param_1 + 0x30),uVar1);
      pbVar7 = *(byte **)(param_1 + 0x30);
      pbVar6 = *(byte **)(param_1 + 0x18);
      for (uVar5 = __n_00; 0xf < uVar5; uVar5 = uVar5 - 0x10) {
        uVar13 = *(undefined8 *)(pbVar6 + 8);
        uVar11 = *(undefined8 *)pbVar6;
        uVar14 = *(undefined8 *)(pbVar7 + 8);
        uVar12 = *(undefined8 *)pbVar7;
        *(ulong *)(pbVar7 + 8) =
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
                                                                   CONCAT11((byte)((ulong)uVar14 >>
                                                                                  8) ^
                                                                            (byte)((ulong)uVar13 >>
                                                                                  8),(byte)uVar14 ^
                                                                                     (byte)uVar13)))
                                                ))));
        *(ulong *)pbVar7 =
             CONCAT17((byte)((ulong)uVar12 >> 0x38) ^ (byte)((ulong)uVar11 >> 0x38),
                      CONCAT16((byte)((ulong)uVar12 >> 0x30) ^ (byte)((ulong)uVar11 >> 0x30),
                               CONCAT15((byte)((ulong)uVar12 >> 0x28) ^
                                        (byte)((ulong)uVar11 >> 0x28),
                                        CONCAT14((byte)((ulong)uVar12 >> 0x20) ^
                                                 (byte)((ulong)uVar11 >> 0x20),
                                                 CONCAT13((byte)((ulong)uVar12 >> 0x18) ^
                                                          (byte)((ulong)uVar11 >> 0x18),
                                                          CONCAT12((byte)((ulong)uVar12 >> 0x10) ^
                                                                   (byte)((ulong)uVar11 >> 0x10),
                                                                   CONCAT11((byte)((ulong)uVar12 >>
                                                                                  8) ^
                                                                            (byte)((ulong)uVar11 >>
                                                                                  8),(byte)uVar12 ^
                                                                                     (byte)uVar11)))
                                                ))));
        pbVar7 = pbVar7 + 0x10;
        pbVar6 = pbVar6 + 0x10;
      }
      if (uVar5 != 0) {
        if ((7 < uVar5) && ((pbVar6 + uVar5 <= pbVar7 || (pbVar7 + uVar5 <= pbVar6)))) {
          uVar9 = uVar5 & 8;
          pbVar3 = pbVar7;
          pbVar4 = pbVar6;
          uVar8 = uVar9;
          do {
            uVar11 = *(undefined8 *)pbVar4;
            uVar13 = *(undefined8 *)pbVar3;
            uVar8 = uVar8 - 8;
            *(ulong *)pbVar3 =
                 CONCAT17((byte)((ulong)uVar13 >> 0x38) ^ (byte)((ulong)uVar11 >> 0x38),
                          CONCAT16((byte)((ulong)uVar13 >> 0x30) ^ (byte)((ulong)uVar11 >> 0x30),
                                   CONCAT15((byte)((ulong)uVar13 >> 0x28) ^
                                            (byte)((ulong)uVar11 >> 0x28),
                                            CONCAT14((byte)((ulong)uVar13 >> 0x20) ^
                                                     (byte)((ulong)uVar11 >> 0x20),
                                                     CONCAT13((byte)((ulong)uVar13 >> 0x18) ^
                                                              (byte)((ulong)uVar11 >> 0x18),
                                                              CONCAT12((byte)((ulong)uVar13 >> 0x10)
                                                                       ^ (byte)((ulong)uVar11 >>
                                                                               0x10),
                                                                       CONCAT11((byte)((ulong)uVar13
                                                                                      >> 8) ^
                                                                                (byte)((ulong)uVar11
                                                                                      >> 8),
                                                                                (byte)uVar13 ^
                                                                                (byte)uVar11)))))));
            pbVar3 = pbVar3 + 8;
            pbVar4 = pbVar4 + 8;
          } while (uVar8 != 0);
          bVar2 = uVar5 == uVar9;
          uVar5 = uVar5 & 7;
          pbVar6 = pbVar6 + uVar9;
          pbVar7 = pbVar7 + uVar9;
          if (bVar2) goto LAB_004bdbf0;
        }
        do {
          uVar5 = uVar5 - 1;
          *pbVar7 = *pbVar7 ^ *pbVar6;
          pbVar6 = pbVar6 + 1;
          pbVar7 = pbVar7 + 1;
        } while (uVar5 != 0);
      }
LAB_004bdbf0:
      pbVar7 = (byte *)(*(long *)(param_1 + 0x30) + __n_00);
      pbVar6 = param_2;
      for (uVar5 = __n - __n_00; 0xf < uVar5; uVar5 = uVar5 - 0x10) {
        uVar13 = *(undefined8 *)(pbVar6 + 8);
        uVar11 = *(undefined8 *)pbVar6;
        uVar14 = *(undefined8 *)(pbVar7 + 8);
        uVar12 = *(undefined8 *)pbVar7;
        *(ulong *)(pbVar7 + 8) =
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
                                                                   CONCAT11((byte)((ulong)uVar14 >>
                                                                                  8) ^
                                                                            (byte)((ulong)uVar13 >>
                                                                                  8),(byte)uVar14 ^
                                                                                     (byte)uVar13)))
                                                ))));
        *(ulong *)pbVar7 =
             CONCAT17((byte)((ulong)uVar12 >> 0x38) ^ (byte)((ulong)uVar11 >> 0x38),
                      CONCAT16((byte)((ulong)uVar12 >> 0x30) ^ (byte)((ulong)uVar11 >> 0x30),
                               CONCAT15((byte)((ulong)uVar12 >> 0x28) ^
                                        (byte)((ulong)uVar11 >> 0x28),
                                        CONCAT14((byte)((ulong)uVar12 >> 0x20) ^
                                                 (byte)((ulong)uVar11 >> 0x20),
                                                 CONCAT13((byte)((ulong)uVar12 >> 0x18) ^
                                                          (byte)((ulong)uVar11 >> 0x18),
                                                          CONCAT12((byte)((ulong)uVar12 >> 0x10) ^
                                                                   (byte)((ulong)uVar11 >> 0x10),
                                                                   CONCAT11((byte)((ulong)uVar12 >>
                                                                                  8) ^
                                                                            (byte)((ulong)uVar11 >>
                                                                                  8),(byte)uVar12 ^
                                                                                     (byte)uVar11)))
                                                ))));
        pbVar7 = pbVar7 + 0x10;
        pbVar6 = pbVar6 + 0x10;
      }
      if (uVar5 != 0) {
        if ((7 < uVar5) && ((pbVar6 + uVar5 <= pbVar7 || (pbVar7 + uVar5 <= pbVar6)))) {
          uVar9 = uVar5 & 8;
          pbVar3 = pbVar7;
          pbVar4 = pbVar6;
          uVar8 = uVar9;
          do {
            uVar11 = *(undefined8 *)pbVar4;
            uVar13 = *(undefined8 *)pbVar3;
            uVar8 = uVar8 - 8;
            *(ulong *)pbVar3 =
                 CONCAT17((byte)((ulong)uVar13 >> 0x38) ^ (byte)((ulong)uVar11 >> 0x38),
                          CONCAT16((byte)((ulong)uVar13 >> 0x30) ^ (byte)((ulong)uVar11 >> 0x30),
                                   CONCAT15((byte)((ulong)uVar13 >> 0x28) ^
                                            (byte)((ulong)uVar11 >> 0x28),
                                            CONCAT14((byte)((ulong)uVar13 >> 0x20) ^
                                                     (byte)((ulong)uVar11 >> 0x20),
                                                     CONCAT13((byte)((ulong)uVar13 >> 0x18) ^
                                                              (byte)((ulong)uVar11 >> 0x18),
                                                              CONCAT12((byte)((ulong)uVar13 >> 0x10)
                                                                       ^ (byte)((ulong)uVar11 >>
                                                                               0x10),
                                                                       CONCAT11((byte)((ulong)uVar13
                                                                                      >> 8) ^
                                                                                (byte)((ulong)uVar11
                                                                                      >> 8),
                                                                                (byte)uVar13 ^
                                                                                (byte)uVar11)))))));
            pbVar3 = pbVar3 + 8;
            pbVar4 = pbVar4 + 8;
          } while (uVar8 != 0);
          bVar2 = uVar5 == uVar9;
          uVar5 = uVar5 & 7;
          pbVar6 = pbVar6 + uVar9;
          pbVar7 = pbVar7 + uVar9;
          if (bVar2) goto LAB_004bdc70;
        }
        do {
          uVar5 = uVar5 - 1;
          *pbVar7 = *pbVar7 ^ *pbVar6;
          pbVar6 = pbVar6 + 1;
          pbVar7 = pbVar7 + 1;
        } while (uVar5 != 0);
      }
LAB_004bdc70:
      memmove(*(void **)(param_1 + 0x18),param_2 + (__n - __n_00),__n_00);
      if (__n != 0) {
        memmove(param_2,*(void **)(param_1 + 0x30),__n);
      }
      uVar10 = uVar10 - uVar1;
      param_2 = param_2 + __n;
    } while (uVar10 != 0);
  }
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004bdadc"></a> `004bdadc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-004bdae0"></a> `004bdae0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004bdae4"></a> `004bdae4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004bdae8"></a> `004bdae8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bdaec"></a> `004bdaec` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bdaf0"></a> `004bdaf0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-004bdaf4"></a> `004bdaf4` | `09 a0 41 a9` | ldp x9,x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-004bdaf8"></a> `004bdaf8` | `15 01 09 cb` | sub x21,x8,x9 | `FALL_THROUGH`
<a id="insn-004bdafc"></a> `004bdafc` | `59 08 d5 9a` | udiv x25,x2,x21 | `FALL_THROUGH`
<a id="insn-004bdb00"></a> `004bdb00` | `28 8b 15 9b` | msub x8,x25,x21,x2 | `FALL_THROUGH`
<a id="insn-004bdb04"></a> `004bdb04` | `28 10 00 b5` | cbnz x8,0x004bdd08 | `CONDITIONAL_JUMP`
<a id="insn-004bdb08"></a> `004bdb08` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-004bdb0c"></a> `004bdb0c` | `bf 02 02 eb` | cmp x21,x2 | `FALL_THROUGH`
<a id="insn-004bdb10"></a> `004bdb10` | `09 01 00 54` | b.ls 0x004bdb30 | `CONDITIONAL_JUMP`
<a id="insn-004bdb14"></a> `004bdb14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bdb18"></a> `004bdb18` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bdb1c"></a> `004bdb1c` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004bdb20"></a> `004bdb20` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bdb24"></a> `004bdb24` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004bdb28"></a> `004bdb28` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-004bdb2c"></a> `004bdb2c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004bdb30"></a> `004bdb30` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004bdb34"></a> `004bdb34` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-004bdb38"></a> `004bdb38` | `04 00 00 14` | b 0x004bdb48 | `UNCONDITIONAL_JUMP`
<a id="insn-004bdb3c"></a> `004bdb3c` | `39 03 18 eb` | subs x25,x25,x24 | `FALL_THROUGH`
<a id="insn-004bdb40"></a> `004bdb40` | `d6 02 17 8b` | add x22,x22,x23 | `FALL_THROUGH`
<a id="insn-004bdb44"></a> `004bdb44` | `80 fe ff 54` | b.eq 0x004bdb14 | `CONDITIONAL_JUMP`
<a id="insn-004bdb48"></a> `004bdb48` | `28 7f 15 9b` | mul x8,x25,x21 | `FALL_THROUGH`
<a id="insn-004bdb4c"></a> `004bdb4c` | `82 26 43 a9` | ldp x2,x9,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-004bdb50"></a> `004bdb50` | `80 06 40 f9` | ldr x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-004bdb54"></a> `004bdb54` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-004bdb58"></a> `004bdb58` | `29 01 02 cb` | sub x9,x9,x2 | `FALL_THROUGH`
<a id="insn-004bdb5c"></a> `004bdb5c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-004bdb60"></a> `004bdb60` | `37 31 88 9a` | csel x23,x9,x8,cc | `FALL_THROUGH`
<a id="insn-004bdb64"></a> `004bdb64` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004bdb68"></a> `004bdb68` | `f8 0a d5 9a` | udiv x24,x23,x21 | `FALL_THROUGH`
<a id="insn-004bdb6c"></a> `004bdb6c` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-004bdb70"></a> `004bdb70` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-004bdb74"></a> `004bdb74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004bdb78"></a> `004bdb78` | `88 1a 40 f9` | ldr x8,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-004bdb7c"></a> `004bdb7c` | `89 0e 40 f9` | ldr x9,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-004bdb80"></a> `004bdb80` | `bf 42 00 f1` | cmp x21,#0x10 | `FALL_THROUGH`
<a id="insn-004bdb84"></a> `004bdb84` | `ea 03 15 aa` | mov x10,x21 | `FALL_THROUGH`
<a id="insn-004bdb88"></a> `004bdb88` | `03 01 00 54` | b.cc 0x004bdba8 | `CONDITIONAL_JUMP`
<a id="insn-004bdb8c"></a> `004bdb8c` | `20 05 c1 3c` | ldr q0,[x9], #0x10 | `FALL_THROUGH`
<a id="insn-004bdb90"></a> `004bdb90` | `01 01 c0 3d` | ldr q1,[x8] | `FALL_THROUGH`
<a id="insn-004bdb94"></a> `004bdb94` | `4a 41 00 d1` | sub x10,x10,#0x10 | `FALL_THROUGH`
<a id="insn-004bdb98"></a> `004bdb98` | `20 1c 20 6e` | eor v0.16B,v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-004bdb9c"></a> `004bdb9c` | `5f 3d 00 f1` | cmp x10,#0xf | `FALL_THROUGH`
<a id="insn-004bdba0"></a> `004bdba0` | `00 05 81 3c` | str q0,[x8], #0x10 | `FALL_THROUGH`
<a id="insn-004bdba4"></a> `004bdba4` | `48 ff ff 54` | b.hi 0x004bdb8c | `CONDITIONAL_JUMP`
<a id="insn-004bdba8"></a> `004bdba8` | `4a 02 00 b4` | cbz x10,0x004bdbf0 | `CONDITIONAL_JUMP`
<a id="insn-004bdbac"></a> `004bdbac` | `5f 21 00 f1` | cmp x10,#0x8 | `FALL_THROUGH`
<a id="insn-004bdbb0"></a> `004bdbb0` | `e3 00 00 54` | b.cc 0x004bdbcc | `CONDITIONAL_JUMP`
<a id="insn-004bdbb4"></a> `004bdbb4` | `2b 01 0a 8b` | add x11,x9,x10 | `FALL_THROUGH`
<a id="insn-004bdbb8"></a> `004bdbb8` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-004bdbbc"></a> `004bdbbc` | `e2 06 00 54` | b.cs 0x004bdc98 | `CONDITIONAL_JUMP`
<a id="insn-004bdbc0"></a> `004bdbc0` | `0b 01 0a 8b` | add x11,x8,x10 | `FALL_THROUGH`
<a id="insn-004bdbc4"></a> `004bdbc4` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-004bdbc8"></a> `004bdbc8` | `82 06 00 54` | b.cs 0x004bdc98 | `CONDITIONAL_JUMP`
<a id="insn-004bdbcc"></a> `004bdbcc` | `eb 03 0a aa` | mov x11,x10 | `FALL_THROUGH`
<a id="insn-004bdbd0"></a> `004bdbd0` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-004bdbd4"></a> `004bdbd4` | `ed 03 08 aa` | mov x13,x8 | `FALL_THROUGH`
<a id="insn-004bdbd8"></a> `004bdbd8` | `88 15 40 38` | ldrb w8,[x12], #0x1 | `FALL_THROUGH`
<a id="insn-004bdbdc"></a> `004bdbdc` | `a9 01 40 39` | ldrb w9,[x13] | `FALL_THROUGH`
<a id="insn-004bdbe0"></a> `004bdbe0` | `6b 05 00 f1` | subs x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-004bdbe4"></a> `004bdbe4` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-004bdbe8"></a> `004bdbe8` | `a8 15 00 38` | strb w8,[x13], #0x1 | `FALL_THROUGH`
<a id="insn-004bdbec"></a> `004bdbec` | `61 ff ff 54` | b.ne 0x004bdbd8 | `CONDITIONAL_JUMP`
<a id="insn-004bdbf0"></a> `004bdbf0` | `89 1a 40 f9` | ldr x9,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-004bdbf4"></a> `004bdbf4` | `e8 02 15 cb` | sub x8,x23,x21 | `FALL_THROUGH`
<a id="insn-004bdbf8"></a> `004bdbf8` | `ea 03 16 aa` | mov x10,x22 | `FALL_THROUGH`
<a id="insn-004bdbfc"></a> `004bdbfc` | `1f 41 00 f1` | cmp x8,#0x10 | `FALL_THROUGH`
<a id="insn-004bdc00"></a> `004bdc00` | `eb 03 08 aa` | mov x11,x8 | `FALL_THROUGH`
<a id="insn-004bdc04"></a> `004bdc04` | `29 01 15 8b` | add x9,x9,x21 | `FALL_THROUGH`
<a id="insn-004bdc08"></a> `004bdc08` | `03 01 00 54` | b.cc 0x004bdc28 | `CONDITIONAL_JUMP`
<a id="insn-004bdc0c"></a> `004bdc0c` | `40 05 c1 3c` | ldr q0,[x10], #0x10 | `FALL_THROUGH`
<a id="insn-004bdc10"></a> `004bdc10` | `21 01 c0 3d` | ldr q1,[x9] | `FALL_THROUGH`
<a id="insn-004bdc14"></a> `004bdc14` | `6b 41 00 d1` | sub x11,x11,#0x10 | `FALL_THROUGH`
<a id="insn-004bdc18"></a> `004bdc18` | `20 1c 20 6e` | eor v0.16B,v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-004bdc1c"></a> `004bdc1c` | `7f 3d 00 f1` | cmp x11,#0xf | `FALL_THROUGH`
<a id="insn-004bdc20"></a> `004bdc20` | `20 05 81 3c` | str q0,[x9], #0x10 | `FALL_THROUGH`
<a id="insn-004bdc24"></a> `004bdc24` | `48 ff ff 54` | b.hi 0x004bdc0c | `CONDITIONAL_JUMP`
<a id="insn-004bdc28"></a> `004bdc28` | `4b 02 00 b4` | cbz x11,0x004bdc70 | `CONDITIONAL_JUMP`
<a id="insn-004bdc2c"></a> `004bdc2c` | `7f 21 00 f1` | cmp x11,#0x8 | `FALL_THROUGH`
<a id="insn-004bdc30"></a> `004bdc30` | `e3 00 00 54` | b.cc 0x004bdc4c | `CONDITIONAL_JUMP`
<a id="insn-004bdc34"></a> `004bdc34` | `4c 01 0b 8b` | add x12,x10,x11 | `FALL_THROUGH`
<a id="insn-004bdc38"></a> `004bdc38` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-004bdc3c"></a> `004bdc3c` | `a2 04 00 54` | b.cs 0x004bdcd0 | `CONDITIONAL_JUMP`
<a id="insn-004bdc40"></a> `004bdc40` | `2c 01 0b 8b` | add x12,x9,x11 | `FALL_THROUGH`
<a id="insn-004bdc44"></a> `004bdc44` | `5f 01 0c eb` | cmp x10,x12 | `FALL_THROUGH`
<a id="insn-004bdc48"></a> `004bdc48` | `42 04 00 54` | b.cs 0x004bdcd0 | `CONDITIONAL_JUMP`
<a id="insn-004bdc4c"></a> `004bdc4c` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-004bdc50"></a> `004bdc50` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-004bdc54"></a> `004bdc54` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-004bdc58"></a> `004bdc58` | `a9 15 40 38` | ldrb w9,[x13], #0x1 | `FALL_THROUGH`
<a id="insn-004bdc5c"></a> `004bdc5c` | `ca 01 40 39` | ldrb w10,[x14] | `FALL_THROUGH`
<a id="insn-004bdc60"></a> `004bdc60` | `8c 05 00 f1` | subs x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-004bdc64"></a> `004bdc64` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-004bdc68"></a> `004bdc68` | `c9 15 00 38` | strb w9,[x14], #0x1 | `FALL_THROUGH`
<a id="insn-004bdc6c"></a> `004bdc6c` | `61 ff ff 54` | b.ne 0x004bdc58 | `CONDITIONAL_JUMP`
<a id="insn-004bdc70"></a> `004bdc70` | `80 0e 40 f9` | ldr x0,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-004bdc74"></a> `004bdc74` | `c1 02 08 8b` | add x1,x22,x8 | `FALL_THROUGH`
<a id="insn-004bdc78"></a> `004bdc78` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-004bdc7c"></a> `004bdc7c` | `d9 6c 1e 94` | bl 0x00c58fe0 | `UNCONDITIONAL_CALL`
<a id="insn-004bdc80"></a> `004bdc80` | `f7 f5 ff b4` | cbz x23,0x004bdb3c | `CONDITIONAL_JUMP`
<a id="insn-004bdc84"></a> `004bdc84` | `81 1a 40 f9` | ldr x1,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-004bdc88"></a> `004bdc88` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-004bdc8c"></a> `004bdc8c` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-004bdc90"></a> `004bdc90` | `d4 6c 1e 94` | bl 0x00c58fe0 | `UNCONDITIONAL_CALL`
<a id="insn-004bdc94"></a> `004bdc94` | `aa ff ff 17` | b 0x004bdb3c | `UNCONDITIONAL_JUMP`
<a id="insn-004bdc98"></a> `004bdc98` | `4e 01 7d 92` | and x14,x10,#0x8 | `FALL_THROUGH`
<a id="insn-004bdc9c"></a> `004bdc9c` | `4b 09 40 92` | and x11,x10,#0x7 | `FALL_THROUGH`
<a id="insn-004bdca0"></a> `004bdca0` | `2c 01 0e 8b` | add x12,x9,x14 | `FALL_THROUGH`
<a id="insn-004bdca4"></a> `004bdca4` | `0d 01 0e 8b` | add x13,x8,x14 | `FALL_THROUGH`
<a id="insn-004bdca8"></a> `004bdca8` | `ef 03 0e aa` | mov x15,x14 | `FALL_THROUGH`
<a id="insn-004bdcac"></a> `004bdcac` | `20 85 40 fc` | ldr d0,[x9], #0x8 | `FALL_THROUGH`
<a id="insn-004bdcb0"></a> `004bdcb0` | `01 01 40 fd` | ldr d1,[x8] | `FALL_THROUGH`
<a id="insn-004bdcb4"></a> `004bdcb4` | `ef 21 00 f1` | subs x15,x15,#0x8 | `FALL_THROUGH`
<a id="insn-004bdcb8"></a> `004bdcb8` | `20 1c 20 2e` | eor v0.8B,v1.8B,v0.8B | `FALL_THROUGH`
<a id="insn-004bdcbc"></a> `004bdcbc` | `00 85 00 fc` | str d0,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-004bdcc0"></a> `004bdcc0` | `61 ff ff 54` | b.ne 0x004bdcac | `CONDITIONAL_JUMP`
<a id="insn-004bdcc4"></a> `004bdcc4` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-004bdcc8"></a> `004bdcc8` | `81 f8 ff 54` | b.ne 0x004bdbd8 | `CONDITIONAL_JUMP`
<a id="insn-004bdccc"></a> `004bdccc` | `c9 ff ff 17` | b 0x004bdbf0 | `UNCONDITIONAL_JUMP`
<a id="insn-004bdcd0"></a> `004bdcd0` | `6f 01 7d 92` | and x15,x11,#0x8 | `FALL_THROUGH`
<a id="insn-004bdcd4"></a> `004bdcd4` | `6c 09 40 92` | and x12,x11,#0x7 | `FALL_THROUGH`
<a id="insn-004bdcd8"></a> `004bdcd8` | `4d 01 0f 8b` | add x13,x10,x15 | `FALL_THROUGH`
<a id="insn-004bdcdc"></a> `004bdcdc` | `2e 01 0f 8b` | add x14,x9,x15 | `FALL_THROUGH`
<a id="insn-004bdce0"></a> `004bdce0` | `f0 03 0f aa` | mov x16,x15 | `FALL_THROUGH`
<a id="insn-004bdce4"></a> `004bdce4` | `40 85 40 fc` | ldr d0,[x10], #0x8 | `FALL_THROUGH`
<a id="insn-004bdce8"></a> `004bdce8` | `21 01 40 fd` | ldr d1,[x9] | `FALL_THROUGH`
<a id="insn-004bdcec"></a> `004bdcec` | `10 22 00 f1` | subs x16,x16,#0x8 | `FALL_THROUGH`
<a id="insn-004bdcf0"></a> `004bdcf0` | `20 1c 20 2e` | eor v0.8B,v1.8B,v0.8B | `FALL_THROUGH`
<a id="insn-004bdcf4"></a> `004bdcf4` | `20 85 00 fc` | str d0,[x9], #0x8 | `FALL_THROUGH`
<a id="insn-004bdcf8"></a> `004bdcf8` | `61 ff ff 54` | b.ne 0x004bdce4 | `CONDITIONAL_JUMP`
<a id="insn-004bdcfc"></a> `004bdcfc` | `7f 01 0f eb` | cmp x11,x15 | `FALL_THROUGH`
<a id="insn-004bdd00"></a> `004bdd00` | `c1 fa ff 54` | b.ne 0x004bdc58 | `CONDITIONAL_JUMP`
<a id="insn-004bdd04"></a> `004bdd04` | `db ff ff 17` | b 0x004bdc70 | `UNCONDITIONAL_JUMP`
<a id="insn-004bdd08"></a> `004bdd08` | `40 ef ff f0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-004bdd0c"></a> `004bdd0c` | `00 70 34 91` | add x0,x0,#0xd1c | `FALL_THROUGH`
<a id="insn-004bdd10"></a> `004bdd10` | `81 ef ff f0` | adrp x1,0x2b0000 | `FALL_THROUGH`
<a id="insn-004bdd14"></a> `004bdd14` | `21 88 2e 91` | add x1,x1,#0xba2 | `FALL_THROUGH`
<a id="insn-004bdd18"></a> `004bdd18` | `22 ef ff f0` | adrp x2,0x2a4000 | `FALL_THROUGH`
<a id="insn-004bdd1c"></a> `004bdd1c` | `42 78 06 91` | add x2,x2,#0x19e | `FALL_THROUGH`
<a id="insn-004bdd20"></a> `004bdd20` | `43 ef ff 90` | adrp x3,0x2a5000 | `FALL_THROUGH`
<a id="insn-004bdd24"></a> `004bdd24` | `63 a8 10 91` | add x3,x3,#0x42a | `FALL_THROUGH`
<a id="insn-004bdd28"></a> `004bdd28` | `e4 a7 82 52` | mov w4,#0x153f | `FALL_THROUGH`
<a id="insn-004bdd2c"></a> `004bdd2c` | `71 6e 1e 94` | bl 0x00c596f0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004bdadc`](#insn-004bdadc) 範囲 `[['004bdadc', '004bdb07']]`
  - `CONDITIONAL_JUMP` [`004bdb04`](#insn-004bdb04) → [`004bdd08`](#insn-004bdd08)
  - `FALL_THROUGH` [`004bdb04`](#insn-004bdb04) → [`004bdb08`](#insn-004bdb08)
- ブロック [`004bdb08`](#insn-004bdb08) 範囲 `[['004bdb08', '004bdb13']]`
  - `CONDITIONAL_JUMP` [`004bdb10`](#insn-004bdb10) → [`004bdb30`](#insn-004bdb30)
  - `FALL_THROUGH` [`004bdb10`](#insn-004bdb10) → [`004bdb14`](#insn-004bdb14)
- ブロック [`004bdb14`](#insn-004bdb14) 範囲 `[['004bdb14', '004bdb2f']]`
- ブロック [`004bdb30`](#insn-004bdb30) 範囲 `[['004bdb30', '004bdb3b']]`
  - `UNCONDITIONAL_JUMP` [`004bdb38`](#insn-004bdb38) → [`004bdb48`](#insn-004bdb48)
- ブロック [`004bdb3c`](#insn-004bdb3c) 範囲 `[['004bdb3c', '004bdb47']]`
  - `CONDITIONAL_JUMP` [`004bdb44`](#insn-004bdb44) → [`004bdb14`](#insn-004bdb14)
  - `FALL_THROUGH` [`004bdb44`](#insn-004bdb44) → [`004bdb48`](#insn-004bdb48)
- ブロック [`004bdb48`](#insn-004bdb48) 範囲 `[['004bdb48', '004bdb8b']]`
  - `CONDITIONAL_JUMP` [`004bdb88`](#insn-004bdb88) → [`004bdba8`](#insn-004bdba8)
  - `FALL_THROUGH` [`004bdb88`](#insn-004bdb88) → [`004bdb8c`](#insn-004bdb8c)
- ブロック [`004bdb8c`](#insn-004bdb8c) 範囲 `[['004bdb8c', '004bdba7']]`
  - `CONDITIONAL_JUMP` [`004bdba4`](#insn-004bdba4) → [`004bdb8c`](#insn-004bdb8c)
  - `FALL_THROUGH` [`004bdba4`](#insn-004bdba4) → [`004bdba8`](#insn-004bdba8)
- ブロック [`004bdba8`](#insn-004bdba8) 範囲 `[['004bdba8', '004bdbab']]`
  - `CONDITIONAL_JUMP` [`004bdba8`](#insn-004bdba8) → [`004bdbf0`](#insn-004bdbf0)
  - `FALL_THROUGH` [`004bdba8`](#insn-004bdba8) → [`004bdbac`](#insn-004bdbac)
- ブロック [`004bdbac`](#insn-004bdbac) 範囲 `[['004bdbac', '004bdbb3']]`
  - `CONDITIONAL_JUMP` [`004bdbb0`](#insn-004bdbb0) → [`004bdbcc`](#insn-004bdbcc)
  - `FALL_THROUGH` [`004bdbb0`](#insn-004bdbb0) → [`004bdbb4`](#insn-004bdbb4)
- ブロック [`004bdbb4`](#insn-004bdbb4) 範囲 `[['004bdbb4', '004bdbbf']]`
  - `CONDITIONAL_JUMP` [`004bdbbc`](#insn-004bdbbc) → [`004bdc98`](#insn-004bdc98)
  - `FALL_THROUGH` [`004bdbbc`](#insn-004bdbbc) → [`004bdbc0`](#insn-004bdbc0)
- ブロック [`004bdbc0`](#insn-004bdbc0) 範囲 `[['004bdbc0', '004bdbcb']]`
  - `CONDITIONAL_JUMP` [`004bdbc8`](#insn-004bdbc8) → [`004bdc98`](#insn-004bdc98)
  - `FALL_THROUGH` [`004bdbc8`](#insn-004bdbc8) → [`004bdbcc`](#insn-004bdbcc)
- ブロック [`004bdbcc`](#insn-004bdbcc) 範囲 `[['004bdbcc', '004bdbd7']]`
  - `FALL_THROUGH` [`004bdbd4`](#insn-004bdbd4) → [`004bdbd8`](#insn-004bdbd8)
- ブロック [`004bdbd8`](#insn-004bdbd8) 範囲 `[['004bdbd8', '004bdbef']]`
  - `CONDITIONAL_JUMP` [`004bdbec`](#insn-004bdbec) → [`004bdbd8`](#insn-004bdbd8)
  - `FALL_THROUGH` [`004bdbec`](#insn-004bdbec) → [`004bdbf0`](#insn-004bdbf0)
- ブロック [`004bdbf0`](#insn-004bdbf0) 範囲 `[['004bdbf0', '004bdc0b']]`
  - `CONDITIONAL_JUMP` [`004bdc08`](#insn-004bdc08) → [`004bdc28`](#insn-004bdc28)
  - `FALL_THROUGH` [`004bdc08`](#insn-004bdc08) → [`004bdc0c`](#insn-004bdc0c)
- ブロック [`004bdc0c`](#insn-004bdc0c) 範囲 `[['004bdc0c', '004bdc27']]`
  - `CONDITIONAL_JUMP` [`004bdc24`](#insn-004bdc24) → [`004bdc0c`](#insn-004bdc0c)
  - `FALL_THROUGH` [`004bdc24`](#insn-004bdc24) → [`004bdc28`](#insn-004bdc28)
- ブロック [`004bdc28`](#insn-004bdc28) 範囲 `[['004bdc28', '004bdc2b']]`
  - `CONDITIONAL_JUMP` [`004bdc28`](#insn-004bdc28) → [`004bdc70`](#insn-004bdc70)
  - `FALL_THROUGH` [`004bdc28`](#insn-004bdc28) → [`004bdc2c`](#insn-004bdc2c)
- ブロック [`004bdc2c`](#insn-004bdc2c) 範囲 `[['004bdc2c', '004bdc33']]`
  - `CONDITIONAL_JUMP` [`004bdc30`](#insn-004bdc30) → [`004bdc4c`](#insn-004bdc4c)
  - `FALL_THROUGH` [`004bdc30`](#insn-004bdc30) → [`004bdc34`](#insn-004bdc34)
- ブロック [`004bdc34`](#insn-004bdc34) 範囲 `[['004bdc34', '004bdc3f']]`
  - `CONDITIONAL_JUMP` [`004bdc3c`](#insn-004bdc3c) → [`004bdcd0`](#insn-004bdcd0)
  - `FALL_THROUGH` [`004bdc3c`](#insn-004bdc3c) → [`004bdc40`](#insn-004bdc40)
- ブロック [`004bdc40`](#insn-004bdc40) 範囲 `[['004bdc40', '004bdc4b']]`
  - `CONDITIONAL_JUMP` [`004bdc48`](#insn-004bdc48) → [`004bdcd0`](#insn-004bdcd0)
  - `FALL_THROUGH` [`004bdc48`](#insn-004bdc48) → [`004bdc4c`](#insn-004bdc4c)
- ブロック [`004bdc4c`](#insn-004bdc4c) 範囲 `[['004bdc4c', '004bdc57']]`
  - `FALL_THROUGH` [`004bdc54`](#insn-004bdc54) → [`004bdc58`](#insn-004bdc58)
- ブロック [`004bdc58`](#insn-004bdc58) 範囲 `[['004bdc58', '004bdc6f']]`
  - `CONDITIONAL_JUMP` [`004bdc6c`](#insn-004bdc6c) → [`004bdc58`](#insn-004bdc58)
  - `FALL_THROUGH` [`004bdc6c`](#insn-004bdc6c) → [`004bdc70`](#insn-004bdc70)
- ブロック [`004bdc70`](#insn-004bdc70) 範囲 `[['004bdc70', '004bdc83']]`
  - `CONDITIONAL_JUMP` [`004bdc80`](#insn-004bdc80) → [`004bdb3c`](#insn-004bdb3c)
  - `FALL_THROUGH` [`004bdc80`](#insn-004bdc80) → [`004bdc84`](#insn-004bdc84)
- ブロック [`004bdc84`](#insn-004bdc84) 範囲 `[['004bdc84', '004bdc97']]`
  - `UNCONDITIONAL_JUMP` [`004bdc94`](#insn-004bdc94) → [`004bdb3c`](#insn-004bdb3c)
- ブロック [`004bdc98`](#insn-004bdc98) 範囲 `[['004bdc98', '004bdcab']]`
  - `FALL_THROUGH` [`004bdca8`](#insn-004bdca8) → [`004bdcac`](#insn-004bdcac)
- ブロック [`004bdcac`](#insn-004bdcac) 範囲 `[['004bdcac', '004bdcc3']]`
  - `CONDITIONAL_JUMP` [`004bdcc0`](#insn-004bdcc0) → [`004bdcac`](#insn-004bdcac)
  - `FALL_THROUGH` [`004bdcc0`](#insn-004bdcc0) → [`004bdcc4`](#insn-004bdcc4)
- ブロック [`004bdcc4`](#insn-004bdcc4) 範囲 `[['004bdcc4', '004bdccb']]`
  - `CONDITIONAL_JUMP` [`004bdcc8`](#insn-004bdcc8) → [`004bdbd8`](#insn-004bdbd8)
  - `FALL_THROUGH` [`004bdcc8`](#insn-004bdcc8) → [`004bdccc`](#insn-004bdccc)
- ブロック [`004bdccc`](#insn-004bdccc) 範囲 `[['004bdccc', '004bdccf']]`
  - `UNCONDITIONAL_JUMP` [`004bdccc`](#insn-004bdccc) → [`004bdbf0`](#insn-004bdbf0)
- ブロック [`004bdcd0`](#insn-004bdcd0) 範囲 `[['004bdcd0', '004bdce3']]`
  - `FALL_THROUGH` [`004bdce0`](#insn-004bdce0) → [`004bdce4`](#insn-004bdce4)
- ブロック [`004bdce4`](#insn-004bdce4) 範囲 `[['004bdce4', '004bdcfb']]`
  - `CONDITIONAL_JUMP` [`004bdcf8`](#insn-004bdcf8) → [`004bdce4`](#insn-004bdce4)
  - `FALL_THROUGH` [`004bdcf8`](#insn-004bdcf8) → [`004bdcfc`](#insn-004bdcfc)
- ブロック [`004bdcfc`](#insn-004bdcfc) 範囲 `[['004bdcfc', '004bdd03']]`
  - `CONDITIONAL_JUMP` [`004bdd00`](#insn-004bdd00) → [`004bdc58`](#insn-004bdc58)
  - `FALL_THROUGH` [`004bdd00`](#insn-004bdd00) → [`004bdd04`](#insn-004bdd04)
- ブロック [`004bdd04`](#insn-004bdd04) 範囲 `[['004bdd04', '004bdd07']]`
  - `UNCONDITIONAL_JUMP` [`004bdd04`](#insn-004bdd04) → [`004bdc70`](#insn-004bdc70)
- ブロック [`004bdd08`](#insn-004bdd08) 範囲 `[['004bdd08', '004bdd2f']]`

## 命令位置別の参照

- [`004bdadc`](#insn-004bdadc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdae0`](#insn-004bdae0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdae4`](#insn-004bdae4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdae8`](#insn-004bdae8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdaec`](#insn-004bdaec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdb04`](#insn-004bdb04) → [`004bdd08`](#insn-004bdd08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdb10`](#insn-004bdb10) → [`004bdb30`](#insn-004bdb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdb18`](#insn-004bdb18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdb1c`](#insn-004bdb1c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdb20`](#insn-004bdb20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdb24`](#insn-004bdb24) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdb28`](#insn-004bdb28) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdb38`](#insn-004bdb38) → [`004bdb48`](#insn-004bdb48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdb44`](#insn-004bdb44) → [`004bdb14`](#insn-004bdb14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdb88`](#insn-004bdb88) → [`004bdba8`](#insn-004bdba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdba4`](#insn-004bdba4) → [`004bdb8c`](#insn-004bdb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdba8`](#insn-004bdba8) → [`004bdbf0`](#insn-004bdbf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdbb0`](#insn-004bdbb0) → [`004bdbcc`](#insn-004bdbcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdbbc`](#insn-004bdbbc) → [`004bdc98`](#insn-004bdc98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdbc8`](#insn-004bdbc8) → [`004bdc98`](#insn-004bdc98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdbec`](#insn-004bdbec) → [`004bdbd8`](#insn-004bdbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdc08`](#insn-004bdc08) → [`004bdc28`](#insn-004bdc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdc24`](#insn-004bdc24) → [`004bdc0c`](#insn-004bdc0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdc28`](#insn-004bdc28) → [`004bdc70`](#insn-004bdc70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdc30`](#insn-004bdc30) → [`004bdc4c`](#insn-004bdc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdc3c`](#insn-004bdc3c) → [`004bdcd0`](#insn-004bdcd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdc48`](#insn-004bdc48) → [`004bdcd0`](#insn-004bdcd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdc6c`](#insn-004bdc6c) → [`004bdc58`](#insn-004bdc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdc7c`](#insn-004bdc7c) → [`00c58fe0`](../00c58/00c58fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58fe0` · 推定シンボル `None` · 推定型 `None`
- [`004bdc80`](#insn-004bdc80) → [`004bdb3c`](#insn-004bdb3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdc90`](#insn-004bdc90) → [`00c58fe0`](../00c58/00c58fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58fe0` · 推定シンボル `None` · 推定型 `None`
- [`004bdc94`](#insn-004bdc94) → [`004bdb3c`](#insn-004bdb3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdcc0`](#insn-004bdcc0) → [`004bdcac`](#insn-004bdcac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdcc8`](#insn-004bdcc8) → [`004bdbd8`](#insn-004bdbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdccc`](#insn-004bdccc) → [`004bdbf0`](#insn-004bdbf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdcf8`](#insn-004bdcf8) → [`004bdce4`](#insn-004bdce4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdd00`](#insn-004bdd00) → [`004bdc58`](#insn-004bdc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdd04`](#insn-004bdd04) → [`004bdc70`](#insn-004bdc70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bdd0c`](#insn-004bdd0c) → `002a8d1c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bdd14`](#insn-004bdd14) → `002b0ba2`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bdd1c`](#insn-004bdd1c) → `002a419e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bdd24`](#insn-004bdd24) → `002a542a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bdd2c`](#insn-004bdd2c) → [`00c596f0`](../00c59/00c596f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c596f0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004bdadc`](#insn-004bdadc)

~~~json
{
  "source": "004bdadc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdae0`](#insn-004bdae0)

~~~json
{
  "source": "004bdae0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdae4`](#insn-004bdae4)

~~~json
{
  "source": "004bdae4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdae8`](#insn-004bdae8)

~~~json
{
  "source": "004bdae8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdaec`](#insn-004bdaec)

~~~json
{
  "source": "004bdaec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdb04`](#insn-004bdb04)

~~~json
{
  "source": "004bdb04",
  "target": "004bdd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdb10`](#insn-004bdb10)

~~~json
{
  "source": "004bdb10",
  "target": "004bdb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdb18`](#insn-004bdb18)

~~~json
{
  "source": "004bdb18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdb1c`](#insn-004bdb1c)

~~~json
{
  "source": "004bdb1c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdb20`](#insn-004bdb20)

~~~json
{
  "source": "004bdb20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdb24`](#insn-004bdb24)

~~~json
{
  "source": "004bdb24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdb28`](#insn-004bdb28)

~~~json
{
  "source": "004bdb28",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdb38`](#insn-004bdb38)

~~~json
{
  "source": "004bdb38",
  "target": "004bdb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdb44`](#insn-004bdb44)

~~~json
{
  "source": "004bdb44",
  "target": "004bdb14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdb88`](#insn-004bdb88)

~~~json
{
  "source": "004bdb88",
  "target": "004bdba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdba4`](#insn-004bdba4)

~~~json
{
  "source": "004bdba4",
  "target": "004bdb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdba8`](#insn-004bdba8)

~~~json
{
  "source": "004bdba8",
  "target": "004bdbf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdbb0`](#insn-004bdbb0)

~~~json
{
  "source": "004bdbb0",
  "target": "004bdbcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdbbc`](#insn-004bdbbc)

~~~json
{
  "source": "004bdbbc",
  "target": "004bdc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdbc8`](#insn-004bdbc8)

~~~json
{
  "source": "004bdbc8",
  "target": "004bdc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdbec`](#insn-004bdbec)

~~~json
{
  "source": "004bdbec",
  "target": "004bdbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdc08`](#insn-004bdc08)

~~~json
{
  "source": "004bdc08",
  "target": "004bdc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdc24`](#insn-004bdc24)

~~~json
{
  "source": "004bdc24",
  "target": "004bdc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdc28`](#insn-004bdc28)

~~~json
{
  "source": "004bdc28",
  "target": "004bdc70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdc30`](#insn-004bdc30)

~~~json
{
  "source": "004bdc30",
  "target": "004bdc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdc3c`](#insn-004bdc3c)

~~~json
{
  "source": "004bdc3c",
  "target": "004bdcd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdc48`](#insn-004bdc48)

~~~json
{
  "source": "004bdc48",
  "target": "004bdcd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdc6c`](#insn-004bdc6c)

~~~json
{
  "source": "004bdc6c",
  "target": "004bdc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdc7c`](#insn-004bdc7c)

~~~json
{
  "source": "004bdc7c",
  "target": "00c58fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bdc80`](#insn-004bdc80)

~~~json
{
  "source": "004bdc80",
  "target": "004bdb3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdc90`](#insn-004bdc90)

~~~json
{
  "source": "004bdc90",
  "target": "00c58fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bdc94`](#insn-004bdc94)

~~~json
{
  "source": "004bdc94",
  "target": "004bdb3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdcc0`](#insn-004bdcc0)

~~~json
{
  "source": "004bdcc0",
  "target": "004bdcac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdcc8`](#insn-004bdcc8)

~~~json
{
  "source": "004bdcc8",
  "target": "004bdbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdccc`](#insn-004bdccc)

~~~json
{
  "source": "004bdccc",
  "target": "004bdbf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdcf8`](#insn-004bdcf8)

~~~json
{
  "source": "004bdcf8",
  "target": "004bdce4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdd00`](#insn-004bdd00)

~~~json
{
  "source": "004bdd00",
  "target": "004bdc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdd04`](#insn-004bdd04)

~~~json
{
  "source": "004bdd04",
  "target": "004bdc70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bdd0c`](#insn-004bdd0c)

~~~json
{
  "source": "004bdd0c",
  "target": "002a8d1c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8d1c",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "737a2025204253203d3d203000",
  "capture_start": "002a8d1c",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bdd14`](#insn-004bdd14)

~~~json
{
  "source": "004bdd14",
  "target": "002b0ba2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0ba2",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "496e7075742069732066756c6c20626c6f636b7300",
  "capture_start": "002b0ba2",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bdd1c`](#insn-004bdd1c)

~~~json
{
  "source": "004bdd1c",
  "target": "002a419e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a419e",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "70726f6365737300",
  "capture_start": "002a419e",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bdd24`](#insn-004bdd24)

~~~json
{
  "source": "004bdd24",
  "target": "002a542a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a542a",
  "offset": 0,
  "size": 141,
  "datatype": "string",
  "bytes": "2f55736572732f626174746c65636174732f2e6a656e6b696e732f776f726b73",
  "capture_start": "002a542a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`004bdd2c`](#insn-004bdd2c)

~~~json
{
  "source": "004bdd2c",
  "target": "00c596f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
