# 005cdecc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `005cde8c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cde8c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0004.md#compare-eb3914f27ddf3590bcd5a2b464dd6dfb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `005ce27c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce27c.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0024.md#compare-7955ccc68ac49f297697aa06d5956744)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005cdecc",
  "name": "FUN_005cdecc",
  "size": 372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "29f394f33b25056d765975f62f67648a12640aa4c0f14cf6f531b69b8e02a09d",
  "source_text_sha256": "29f394f33b25056d765975f62f67648a12640aa4c0f14cf6f531b69b8e02a09d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005cdecc",
        "005ce03f"
      ]
    ],
    "bytes_sha256": "f4d44a1d94b9eb42f4667a3469b300c9ace53d85bba71ce9e66149c481826a68",
    "instruction_count": 93,
    "instruction_bytes": 372,
    "body_bytes": 372,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005cd7f8](../005cd/005cd7f8.md)
- [005ce1f4](../005ce/005ce1f4.md)
- [005d58ac](../005d5/005d58ac.md)

## 呼び出し先

- [005d51f0](../005d5/005d51f0.md)
- [005d58ac](../005d5/005d58ac.md)
- [00c57f60](../00c57/00c57f60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3902 bytes

~~~c

char * FUN_005cdecc(long param_1,char *param_2,char *param_3)

{
  undefined *puVar1;
  undefined *puVar2;
  undefined *puVar3;
  char *pcVar4;
  char *pcVar5;
  long *plVar6;
  long lVar7;
  long lVar8;
  char *pcVar9;
  long lVar10;
  long lVar11;
  
  lVar10 = *(long *)(param_1 + 0x38);
  pcVar4 = (char *)FUN_005d58ac();
  if (pcVar4 != param_2) {
    do {
      pcVar9 = pcVar4;
      pcVar4 = (char *)FUN_005d58ac(param_1,pcVar9,param_3);
    } while (pcVar4 != pcVar9);
    if (pcVar9 != param_2) {
      if (pcVar9 != param_3) {
        puVar1 = PTR__ZTVNSt6__ndk111__alternateIcEE_00c9b468 + 0x10;
        puVar2 = PTR__ZTVNSt6__ndk113__empty_stateIcEE_00c9b458 + 0x10;
        puVar3 = PTR__ZTVNSt6__ndk121__empty_non_own_stateIcEE_00c9b470 + 0x10;
        do {
          if (*pcVar9 != '|') {
            return pcVar9;
          }
          pcVar4 = pcVar9 + 1;
          lVar11 = *(long *)(param_1 + 0x38);
          pcVar5 = (char *)FUN_005d58ac(param_1,pcVar4,param_3);
          if (pcVar5 == pcVar4) goto LAB_005ce03c;
          do {
            pcVar9 = pcVar5;
                    /* try { // try from 005cdf88 to 006cdf8f has its CatchHandler @ 005ce008 */
            pcVar5 = (char *)FUN_005d58ac(param_1,pcVar9,param_3);
          } while (pcVar5 != pcVar9);
                    /* try { // try from 005cdfa0 to 006cdfa7 has its CatchHandler @ 005cdfc8 */
          if (pcVar9 == pcVar4) goto LAB_005ce03c;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cdeb8 with catch @ 005cdfa8
                       try { // try from 005cdfa8 to 006ce08f has its CatchHandler @ 005cdc6c */
          plVar6 = (long *)_Znwm(0x18);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cddd0 with catch @ 005cdfac
                        */
          lVar7 = *(long *)(lVar11 + 8);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cde2c with catch @ 005cdfb0
                        */
          lVar8 = *(long *)(lVar10 + 8);
          *plVar6 = (long)puVar1;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cddf0 with catch @ 005cdfb8
                        */
          plVar6[1] = lVar8;
          plVar6[2] = lVar7;
          *(long **)(lVar10 + 8) = plVar6;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cdd48 with catch @ 005cdfc0
                        */
          *(undefined8 *)(lVar11 + 8) = 0;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cde58 with catch @ 005cdfc8
                       catch(type#1 @ 00000000) { ... } // from try @ 005cdfa0 with catch @ 005cdfc8
                        */
          plVar6 = (long *)_Znwm(0x10);
          lVar7 = *(long *)(param_1 + 0x38);
          *plVar6 = (long)puVar2;
          plVar6[1] = *(long *)(lVar7 + 8);
          *(long **)(lVar11 + 8) = plVar6;
          *(undefined8 *)(*(long *)(param_1 + 0x38) + 8) = 0;
          plVar6 = (long *)_Znwm(0x10);
          lVar7 = *(long *)(lVar11 + 8);
          lVar8 = *(long *)(param_1 + 0x38);
          *plVar6 = (long)puVar3;
          plVar6[1] = lVar7;
          *(long **)(lVar8 + 8) = plVar6;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cdd68 with catch @ 005ce008
                       catch(type#1 @ 00000000) { ... } // from try @ 005cdf88 with catch @ 005ce008
                        */
          *(undefined8 *)(param_1 + 0x38) = *(undefined8 *)(lVar11 + 8);
        } while (pcVar9 != param_3);
      }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cdd24 with catch @ 005ce02c
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cdd04 with catch @ 005ce030
                        */
      return param_3;
    }
  }
LAB_005ce03c:
                    /* WARNING: Subroutine does not return */
  FUN_005d51f0();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005cdecc"></a> `005cdecc` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-005cded0"></a> `005cded0` | `fb 0b 00 f9` | str x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005cded4"></a> `005cded4` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005cded8"></a> `005cded8` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005cdedc"></a> `005cdedc` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005cdee0"></a> `005cdee0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005cdee4"></a> `005cdee4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005cdee8"></a> `005cdee8` | `17 1c 40 f9` | ldr x23,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-005cdeec"></a> `005cdeec` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-005cdef0"></a> `005cdef0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-005cdef4"></a> `005cdef4` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-005cdef8"></a> `005cdef8` | `6d 1e 00 94` | bl 0x005d58ac | `UNCONDITIONAL_CALL`
<a id="insn-005cdefc"></a> `005cdefc` | `1f 00 16 eb` | cmp x0,x22 | `FALL_THROUGH`
<a id="insn-005cdf00"></a> `005cdf00` | `e0 09 00 54` | b.eq 0x005ce03c | `CONDITIONAL_JUMP`
<a id="insn-005cdf04"></a> `005cdf04` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-005cdf08"></a> `005cdf08` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005cdf0c"></a> `005cdf0c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-005cdf10"></a> `005cdf10` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-005cdf14"></a> `005cdf14` | `66 1e 00 94` | bl 0x005d58ac | `UNCONDITIONAL_CALL`
<a id="insn-005cdf18"></a> `005cdf18` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-005cdf1c"></a> `005cdf1c` | `41 ff ff 54` | b.ne 0x005cdf04 | `CONDITIONAL_JUMP`
<a id="insn-005cdf20"></a> `005cdf20` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-005cdf24"></a> `005cdf24` | `c0 08 00 54` | b.eq 0x005ce03c | `CONDITIONAL_JUMP`
<a id="insn-005cdf28"></a> `005cdf28` | `bf 02 13 eb` | cmp x21,x19 | `FALL_THROUGH`
<a id="insn-005cdf2c"></a> `005cdf2c` | `80 07 00 54` | b.eq 0x005ce01c | `CONDITIONAL_JUMP`
<a id="insn-005cdf30"></a> `005cdf30` | `68 36 00 d0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-005cdf34"></a> `005cdf34` | `69 36 00 d0` | adrp x9,0xc9b000 | `FALL_THROUGH`
<a id="insn-005cdf38"></a> `005cdf38` | `6a 36 00 d0` | adrp x10,0xc9b000 | `FALL_THROUGH`
<a id="insn-005cdf3c"></a> `005cdf3c` | `08 35 42 f9` | ldr x8,[x8, #0x468] | `FALL_THROUGH`
<a id="insn-005cdf40"></a> `005cdf40` | `29 2d 42 f9` | ldr x9,[x9, #0x458] | `FALL_THROUGH`
<a id="insn-005cdf44"></a> `005cdf44` | `4a 39 42 f9` | ldr x10,[x10, #0x470] | `FALL_THROUGH`
<a id="insn-005cdf48"></a> `005cdf48` | `18 41 00 91` | add x24,x8,#0x10 | `FALL_THROUGH`
<a id="insn-005cdf4c"></a> `005cdf4c` | `39 41 00 91` | add x25,x9,#0x10 | `FALL_THROUGH`
<a id="insn-005cdf50"></a> `005cdf50` | `5a 41 00 91` | add x26,x10,#0x10 | `FALL_THROUGH`
<a id="insn-005cdf54"></a> `005cdf54` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-005cdf58"></a> `005cdf58` | `1f f1 01 71` | cmp w8,#0x7c | `FALL_THROUGH`
<a id="insn-005cdf5c"></a> `005cdf5c` | `e1 05 00 54` | b.ne 0x005ce018 | `CONDITIONAL_JUMP`
<a id="insn-005cdf60"></a> `005cdf60` | `b6 06 00 91` | add x22,x21,#0x1 | `FALL_THROUGH`
<a id="insn-005cdf64"></a> `005cdf64` | `9b 1e 40 f9` | ldr x27,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-005cdf68"></a> `005cdf68` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005cdf6c"></a> `005cdf6c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-005cdf70"></a> `005cdf70` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-005cdf74"></a> `005cdf74` | `4e 1e 00 94` | bl 0x005d58ac | `UNCONDITIONAL_CALL`
<a id="insn-005cdf78"></a> `005cdf78` | `1f 00 16 eb` | cmp x0,x22 | `FALL_THROUGH`
<a id="insn-005cdf7c"></a> `005cdf7c` | `00 06 00 54` | b.eq 0x005ce03c | `CONDITIONAL_JUMP`
<a id="insn-005cdf80"></a> `005cdf80` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-005cdf84"></a> `005cdf84` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005cdf88"></a> `005cdf88` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-005cdf8c"></a> `005cdf8c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-005cdf90"></a> `005cdf90` | `47 1e 00 94` | bl 0x005d58ac | `UNCONDITIONAL_CALL`
<a id="insn-005cdf94"></a> `005cdf94` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-005cdf98"></a> `005cdf98` | `41 ff ff 54` | b.ne 0x005cdf80 | `CONDITIONAL_JUMP`
<a id="insn-005cdf9c"></a> `005cdf9c` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-005cdfa0"></a> `005cdfa0` | `e0 04 00 54` | b.eq 0x005ce03c | `CONDITIONAL_JUMP`
<a id="insn-005cdfa4"></a> `005cdfa4` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-005cdfa8"></a> `005cdfa8` | `ee 27 1a 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-005cdfac"></a> `005cdfac` | `68 07 40 f9` | ldr x8,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-005cdfb0"></a> `005cdfb0` | `e9 06 40 f9` | ldr x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-005cdfb4"></a> `005cdfb4` | `18 00 00 f9` | str x24,[x0] | `FALL_THROUGH`
<a id="insn-005cdfb8"></a> `005cdfb8` | `09 a0 00 a9` | stp x9,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-005cdfbc"></a> `005cdfbc` | `e0 06 00 f9` | str x0,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-005cdfc0"></a> `005cdfc0` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-005cdfc4"></a> `005cdfc4` | `7f 07 00 f9` | str xzr,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-005cdfc8"></a> `005cdfc8` | `e6 27 1a 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-005cdfcc"></a> `005cdfcc` | `88 1e 40 f9` | ldr x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-005cdfd0"></a> `005cdfd0` | `19 00 00 f9` | str x25,[x0] | `FALL_THROUGH`
<a id="insn-005cdfd4"></a> `005cdfd4` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-005cdfd8"></a> `005cdfd8` | `08 04 00 f9` | str x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-005cdfdc"></a> `005cdfdc` | `60 07 00 f9` | str x0,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-005cdfe0"></a> `005cdfe0` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-005cdfe4"></a> `005cdfe4` | `88 1e 40 f9` | ldr x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-005cdfe8"></a> `005cdfe8` | `1f 05 00 f9` | str xzr,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-005cdfec"></a> `005cdfec` | `dd 27 1a 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-005cdff0"></a> `005cdff0` | `68 07 40 f9` | ldr x8,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-005cdff4"></a> `005cdff4` | `89 1e 40 f9` | ldr x9,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-005cdff8"></a> `005cdff8` | `bf 02 13 eb` | cmp x21,x19 | `FALL_THROUGH`
<a id="insn-005cdffc"></a> `005cdffc` | `1a 00 00 f9` | str x26,[x0] | `FALL_THROUGH`
<a id="insn-005ce000"></a> `005ce000` | `08 04 00 f9` | str x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-005ce004"></a> `005ce004` | `20 05 00 f9` | str x0,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-005ce008"></a> `005ce008` | `68 07 40 f9` | ldr x8,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-005ce00c"></a> `005ce00c` | `88 1e 00 f9` | str x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-005ce010"></a> `005ce010` | `21 fa ff 54` | b.ne 0x005cdf54 | `CONDITIONAL_JUMP`
<a id="insn-005ce014"></a> `005ce014` | `02 00 00 14` | b 0x005ce01c | `UNCONDITIONAL_JUMP`
<a id="insn-005ce018"></a> `005ce018` | `f3 03 15 aa` | mov x19,x21 | `FALL_THROUGH`
<a id="insn-005ce01c"></a> `005ce01c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005ce020"></a> `005ce020` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005ce024"></a> `005ce024` | `fb 0b 40 f9` | ldr x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005ce028"></a> `005ce028` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005ce02c"></a> `005ce02c` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005ce030"></a> `005ce030` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005ce034"></a> `005ce034` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-005ce038"></a> `005ce038` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-005ce03c"></a> `005ce03c` | `6d 1c 00 94` | bl 0x005d51f0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005cdecc`](#insn-005cdecc) 範囲 `[['005cdecc', '005cdf03']]`
  - `CONDITIONAL_JUMP` [`005cdf00`](#insn-005cdf00) → [`005ce03c`](#insn-005ce03c)
  - `FALL_THROUGH` [`005cdf00`](#insn-005cdf00) → [`005cdf04`](#insn-005cdf04)
- ブロック [`005cdf04`](#insn-005cdf04) 範囲 `[['005cdf04', '005cdf1f']]`
  - `CONDITIONAL_JUMP` [`005cdf1c`](#insn-005cdf1c) → [`005cdf04`](#insn-005cdf04)
  - `FALL_THROUGH` [`005cdf1c`](#insn-005cdf1c) → [`005cdf20`](#insn-005cdf20)
- ブロック [`005cdf20`](#insn-005cdf20) 範囲 `[['005cdf20', '005cdf27']]`
  - `CONDITIONAL_JUMP` [`005cdf24`](#insn-005cdf24) → [`005ce03c`](#insn-005ce03c)
  - `FALL_THROUGH` [`005cdf24`](#insn-005cdf24) → [`005cdf28`](#insn-005cdf28)
- ブロック [`005cdf28`](#insn-005cdf28) 範囲 `[['005cdf28', '005cdf2f']]`
  - `CONDITIONAL_JUMP` [`005cdf2c`](#insn-005cdf2c) → [`005ce01c`](#insn-005ce01c)
  - `FALL_THROUGH` [`005cdf2c`](#insn-005cdf2c) → [`005cdf30`](#insn-005cdf30)
- ブロック [`005cdf30`](#insn-005cdf30) 範囲 `[['005cdf30', '005cdf53']]`
  - `FALL_THROUGH` [`005cdf50`](#insn-005cdf50) → [`005cdf54`](#insn-005cdf54)
- ブロック [`005cdf54`](#insn-005cdf54) 範囲 `[['005cdf54', '005cdf5f']]`
  - `CONDITIONAL_JUMP` [`005cdf5c`](#insn-005cdf5c) → [`005ce018`](#insn-005ce018)
  - `FALL_THROUGH` [`005cdf5c`](#insn-005cdf5c) → [`005cdf60`](#insn-005cdf60)
- ブロック [`005cdf60`](#insn-005cdf60) 範囲 `[['005cdf60', '005cdf7f']]`
  - `CONDITIONAL_JUMP` [`005cdf7c`](#insn-005cdf7c) → [`005ce03c`](#insn-005ce03c)
  - `FALL_THROUGH` [`005cdf7c`](#insn-005cdf7c) → [`005cdf80`](#insn-005cdf80)
- ブロック [`005cdf80`](#insn-005cdf80) 範囲 `[['005cdf80', '005cdf87']]`
  - `FALL_THROUGH` [`005cdf84`](#insn-005cdf84) → [`005cdf88`](#insn-005cdf88)
- ブロック [`005cdf88`](#insn-005cdf88) 範囲 `[['005cdf88', '005cdf9b']]`
  - `CONDITIONAL_JUMP` [`005cdf98`](#insn-005cdf98) → [`005cdf80`](#insn-005cdf80)
  - `FALL_THROUGH` [`005cdf98`](#insn-005cdf98) → [`005cdf9c`](#insn-005cdf9c)
- ブロック [`005cdf9c`](#insn-005cdf9c) 範囲 `[['005cdf9c', '005cdf9f']]`
  - `FALL_THROUGH` [`005cdf9c`](#insn-005cdf9c) → [`005cdfa0`](#insn-005cdfa0)
- ブロック [`005cdfa0`](#insn-005cdfa0) 範囲 `[['005cdfa0', '005cdfa3']]`
  - `CONDITIONAL_JUMP` [`005cdfa0`](#insn-005cdfa0) → [`005ce03c`](#insn-005ce03c)
  - `FALL_THROUGH` [`005cdfa0`](#insn-005cdfa0) → [`005cdfa4`](#insn-005cdfa4)
- ブロック [`005cdfa4`](#insn-005cdfa4) 範囲 `[['005cdfa4', '005cdfa7']]`
  - `FALL_THROUGH` [`005cdfa4`](#insn-005cdfa4) → [`005cdfa8`](#insn-005cdfa8)
- ブロック [`005cdfa8`](#insn-005cdfa8) 範囲 `[['005cdfa8', '005cdfab']]`
  - `FALL_THROUGH` [`005cdfa8`](#insn-005cdfa8) → [`005cdfac`](#insn-005cdfac)
- ブロック [`005cdfac`](#insn-005cdfac) 範囲 `[['005cdfac', '005cdfaf']]`
  - `FALL_THROUGH` [`005cdfac`](#insn-005cdfac) → [`005cdfb0`](#insn-005cdfb0)
- ブロック [`005cdfb0`](#insn-005cdfb0) 範囲 `[['005cdfb0', '005cdfb7']]`
  - `FALL_THROUGH` [`005cdfb4`](#insn-005cdfb4) → [`005cdfb8`](#insn-005cdfb8)
- ブロック [`005cdfb8`](#insn-005cdfb8) 範囲 `[['005cdfb8', '005cdfbf']]`
  - `FALL_THROUGH` [`005cdfbc`](#insn-005cdfbc) → [`005cdfc0`](#insn-005cdfc0)
- ブロック [`005cdfc0`](#insn-005cdfc0) 範囲 `[['005cdfc0', '005cdfc7']]`
  - `FALL_THROUGH` [`005cdfc4`](#insn-005cdfc4) → [`005cdfc8`](#insn-005cdfc8)
- ブロック [`005cdfc8`](#insn-005cdfc8) 範囲 `[['005cdfc8', '005ce007']]`
  - `FALL_THROUGH` [`005ce004`](#insn-005ce004) → [`005ce008`](#insn-005ce008)
- ブロック [`005ce008`](#insn-005ce008) 範囲 `[['005ce008', '005ce013']]`
  - `CONDITIONAL_JUMP` [`005ce010`](#insn-005ce010) → [`005cdf54`](#insn-005cdf54)
  - `FALL_THROUGH` [`005ce010`](#insn-005ce010) → [`005ce014`](#insn-005ce014)
- ブロック [`005ce014`](#insn-005ce014) 範囲 `[['005ce014', '005ce017']]`
  - `UNCONDITIONAL_JUMP` [`005ce014`](#insn-005ce014) → [`005ce01c`](#insn-005ce01c)
- ブロック [`005ce018`](#insn-005ce018) 範囲 `[['005ce018', '005ce01b']]`
  - `FALL_THROUGH` [`005ce018`](#insn-005ce018) → [`005ce01c`](#insn-005ce01c)
- ブロック [`005ce01c`](#insn-005ce01c) 範囲 `[['005ce01c', '005ce02b']]`
  - `FALL_THROUGH` [`005ce028`](#insn-005ce028) → [`005ce02c`](#insn-005ce02c)
- ブロック [`005ce02c`](#insn-005ce02c) 範囲 `[['005ce02c', '005ce02f']]`
  - `FALL_THROUGH` [`005ce02c`](#insn-005ce02c) → [`005ce030`](#insn-005ce030)
- ブロック [`005ce030`](#insn-005ce030) 範囲 `[['005ce030', '005ce03b']]`
- ブロック [`005ce03c`](#insn-005ce03c) 範囲 `[['005ce03c', '005ce03f']]`

## 命令位置別の参照

- [`005cdecc`](#insn-005cdecc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cded0`](#insn-005cded0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cded4`](#insn-005cded4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cded8`](#insn-005cded8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdedc`](#insn-005cdedc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdee0`](#insn-005cdee0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdef8`](#insn-005cdef8) → [`005d58ac`](../005d5/005d58ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d58ac` · 推定シンボル `None` · 推定型 `None`
- [`005cdf00`](#insn-005cdf00) → [`005ce03c`](#insn-005ce03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf14`](#insn-005cdf14) → [`005d58ac`](../005d5/005d58ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d58ac` · 推定シンボル `None` · 推定型 `None`
- [`005cdf1c`](#insn-005cdf1c) → [`005cdf04`](#insn-005cdf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf24`](#insn-005cdf24) → [`005ce03c`](#insn-005ce03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf2c`](#insn-005cdf2c) → [`005ce01c`](#insn-005ce01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf3c`](#insn-005cdf3c) → `00c9b468`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005cdf40`](#insn-005cdf40) → `00c9b458`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005cdf44`](#insn-005cdf44) → `00c9b470`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005cdf5c`](#insn-005cdf5c) → [`005ce018`](#insn-005ce018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf74`](#insn-005cdf74) → [`005d58ac`](../005d5/005d58ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d58ac` · 推定シンボル `None` · 推定型 `None`
- [`005cdf7c`](#insn-005cdf7c) → [`005ce03c`](#insn-005ce03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf90`](#insn-005cdf90) → [`005d58ac`](../005d5/005d58ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d58ac` · 推定シンボル `None` · 推定型 `None`
- [`005cdf98`](#insn-005cdf98) → [`005cdf80`](#insn-005cdf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdfa0`](#insn-005cdfa0) → [`005ce03c`](#insn-005ce03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdfa8`](#insn-005cdfa8) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`005cdfb4`](#insn-005cdfb4) → `00c71180`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[48]`
- [`005cdfc8`](#insn-005cdfc8) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`005cdfd0`](#insn-005cdfd0) → `00c70c10`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[48]`
- [`005cdfec`](#insn-005cdfec) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`005cdffc`](#insn-005cdffc) → `00c711c8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[48]`
- [`005ce010`](#insn-005ce010) → [`005cdf54`](#insn-005cdf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ce014`](#insn-005ce014) → [`005ce01c`](#insn-005ce01c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ce020`](#insn-005ce020) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ce024`](#insn-005ce024) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ce028`](#insn-005ce028) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ce02c`](#insn-005ce02c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ce030`](#insn-005ce030) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ce034`](#insn-005ce034) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ce03c`](#insn-005ce03c) → [`005d51f0`](../005d5/005d51f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d51f0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005cdecc`](#insn-005cdecc)

~~~json
{
  "source": "005cdecc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cded0`](#insn-005cded0)

~~~json
{
  "source": "005cded0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cded4`](#insn-005cded4)

~~~json
{
  "source": "005cded4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cded8`](#insn-005cded8)

~~~json
{
  "source": "005cded8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdedc`](#insn-005cdedc)

~~~json
{
  "source": "005cdedc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdee0`](#insn-005cdee0)

~~~json
{
  "source": "005cdee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdef8`](#insn-005cdef8)

~~~json
{
  "source": "005cdef8",
  "target": "005d58ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdf00`](#insn-005cdf00)

~~~json
{
  "source": "005cdf00",
  "target": "005ce03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf14`](#insn-005cdf14)

~~~json
{
  "source": "005cdf14",
  "target": "005d58ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdf1c`](#insn-005cdf1c)

~~~json
{
  "source": "005cdf1c",
  "target": "005cdf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf24`](#insn-005cdf24)

~~~json
{
  "source": "005cdf24",
  "target": "005ce03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf2c`](#insn-005cdf2c)

~~~json
{
  "source": "005cdf2c",
  "target": "005ce01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf3c`](#insn-005cdf3c)

~~~json
{
  "source": "005cdf3c",
  "target": "00c9b468",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b468",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005cdf40`](#insn-005cdf40)

~~~json
{
  "source": "005cdf40",
  "target": "00c9b458",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b458",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005cdf44`](#insn-005cdf44)

~~~json
{
  "source": "005cdf44",
  "target": "00c9b470",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b470",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005cdf5c`](#insn-005cdf5c)

~~~json
{
  "source": "005cdf5c",
  "target": "005ce018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf74`](#insn-005cdf74)

~~~json
{
  "source": "005cdf74",
  "target": "005d58ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdf7c`](#insn-005cdf7c)

~~~json
{
  "source": "005cdf7c",
  "target": "005ce03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf90`](#insn-005cdf90)

~~~json
{
  "source": "005cdf90",
  "target": "005d58ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdf98`](#insn-005cdf98)

~~~json
{
  "source": "005cdf98",
  "target": "005cdf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdfa0`](#insn-005cdfa0)

~~~json
{
  "source": "005cdfa0",
  "target": "005ce03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdfa8`](#insn-005cdfa8)

~~~json
{
  "source": "005cdfa8",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdfb4`](#insn-005cdfb4)

~~~json
{
  "source": "005cdfb4",
  "target": "00c71180",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c71170",
  "offset": 16,
  "size": 48,
  "datatype": "undefined1[48]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`005cdfc8`](#insn-005cdfc8)

~~~json
{
  "source": "005cdfc8",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdfd0`](#insn-005cdfd0)

~~~json
{
  "source": "005cdfd0",
  "target": "00c70c10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c70c00",
  "offset": 16,
  "size": 48,
  "datatype": "undefined1[48]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`005cdfec`](#insn-005cdfec)

~~~json
{
  "source": "005cdfec",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdffc`](#insn-005cdffc)

~~~json
{
  "source": "005cdffc",
  "target": "00c711c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c711b8",
  "offset": 16,
  "size": 48,
  "datatype": "undefined1[48]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`005ce010`](#insn-005ce010)

~~~json
{
  "source": "005ce010",
  "target": "005cdf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ce014`](#insn-005ce014)

~~~json
{
  "source": "005ce014",
  "target": "005ce01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ce020`](#insn-005ce020)

~~~json
{
  "source": "005ce020",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ce024`](#insn-005ce024)

~~~json
{
  "source": "005ce024",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ce028`](#insn-005ce028)

~~~json
{
  "source": "005ce028",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ce02c`](#insn-005ce02c)

~~~json
{
  "source": "005ce02c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ce030`](#insn-005ce030)

~~~json
{
  "source": "005ce030",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ce034`](#insn-005ce034)

~~~json
{
  "source": "005ce034",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ce03c`](#insn-005ce03c)

~~~json
{
  "source": "005ce03c",
  "target": "005d51f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
