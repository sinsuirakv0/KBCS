# 00acb5bc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acb54c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb54c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-0a59bb60fec1e93a2aefcc79a56ac106)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00acc5b0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc5b0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-b20d18dbf84886bea94d7ef8c72043e0)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acb5bc",
  "name": "FUN_00acb5bc",
  "size": 340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fd0e0a7b69894b5ecb65515f7850890b1551c75360e91d754865fd6689846a07",
  "source_text_sha256": "fd0e0a7b69894b5ecb65515f7850890b1551c75360e91d754865fd6689846a07",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acb5bc",
        "00acb70f"
      ]
    ],
    "bytes_sha256": "d680eaba4c6d5190470105e8224cad8d2e10feaecc191e3c2a58d47a567279b3",
    "instruction_count": 85,
    "instruction_bytes": 340,
    "body_bytes": 340,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [0047d1fc](../0047d/0047d1fc.md)
- [00851550](../00851/00851550.md)
- [00b3bf30](../00b3b/00b3bf30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1676 bytes

~~~c

void FUN_00acb5bc(undefined8 param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  undefined8 uVar2;
  long lVar3;
  undefined8 uVar4;
  
  iVar1 = *param_3;
  if (iVar1 != 4) {
    if (iVar1 == 3) {
      uVar2 = FUN_0047ad34();
      uVar4 = 0xb;
    }
    else {
      if (iVar1 != 0) {
        return;
      }
      uVar2 = FUN_0047ad34();
      uVar4 = 10;
    }
    FUN_0047ce14(uVar2,uVar4,0);
    return;
  }
  lVar3 = FUN_00851550();
  iVar1 = *(int *)(lVar3 + 0x4a818);
  lVar3 = FUN_00851550();
  if (iVar1 != 0) {
    iVar1 = FUN_00b3bf30(lVar3 + 0xc400);
    lVar3 = FUN_00851550();
    if (iVar1 < 900000) {
      *(undefined4 *)(lVar3 + 0x3478) = 0;
      lVar3 = FUN_00851550();
      *(undefined1 *)(lVar3 + 0x3480) = 1;
    }
    else {
      *(undefined1 *)((long)&fde_table_entry_00335f18.initial_loc + lVar3 + 2) = 1;
      lVar3 = FUN_00851550();
      *(undefined4 *)((long)&fde_table_entry_00335f30.data_loc + lVar3) = 10000;
    }
    return;
  }
  *(undefined4 *)(lVar3 + 0x4a818) = 1;
  lVar3 = FUN_00851550();
  *(undefined1 *)((long)&fde_table_entry_00336f50.data_loc + lVar3) = 1;
  FUN_00851550();
  lVar3 = FUN_00851550();
  *(undefined4 *)((long)&fde_table_entry_00336f58.initial_loc + lVar3) = 0;
  FUN_00851550();
  lVar3 = FUN_00851550();
  *(undefined4 *)((long)&fde_table_entry_00336f58.data_loc + lVar3) = 0;
  FUN_00851550();
  lVar3 = FUN_00851550();
  *(undefined4 *)((long)&fde_table_entry_00336f60.initial_loc + lVar3) = 0;
  FUN_00851550();
  lVar3 = FUN_00851550();
  *(undefined4 *)((long)&fde_table_entry_00336f60.data_loc + lVar3) = 0;
  FUN_00851550();
  uVar2 = FUN_0047ad34();
  FUN_0047d1fc(uVar2,0x32);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acb5bc"></a> `00acb5bc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00acb5c0"></a> `00acb5c0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb5c4"></a> `00acb5c4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acb5c8"></a> `00acb5c8` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00acb5cc"></a> `00acb5cc` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00acb5d0"></a> `00acb5d0` | `a0 01 00 54` | b.eq 0x00acb604 | `CONDITIONAL_JUMP`
<a id="insn-00acb5d4"></a> `00acb5d4` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00acb5d8"></a> `00acb5d8` | `a0 00 00 54` | b.eq 0x00acb5ec | `CONDITIONAL_JUMP`
<a id="insn-00acb5dc"></a> `00acb5dc` | `48 09 00 35` | cbnz w8,0x00acb704 | `CONDITIONAL_JUMP`
<a id="insn-00acb5e0"></a> `00acb5e0` | `d5 bd e6 97` | bl 0x0047ad34 | `UNCONDITIONAL_CALL`
<a id="insn-00acb5e4"></a> `00acb5e4` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00acb5e8"></a> `00acb5e8` | `03 00 00 14` | b 0x00acb5f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acb5ec"></a> `00acb5ec` | `d2 bd e6 97` | bl 0x0047ad34 | `UNCONDITIONAL_CALL`
<a id="insn-00acb5f0"></a> `00acb5f0` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00acb5f4"></a> `00acb5f4` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00acb5f8"></a> `00acb5f8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb5fc"></a> `00acb5fc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acb600"></a> `00acb600` | `05 c6 e6 17` | b 0x0047ce14 | `CALL_TERMINATOR`
<a id="insn-00acb604"></a> `00acb604` | `d3 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb608"></a> `00acb608` | `08 03 95 52` | mov w8,#0xa818 | `FALL_THROUGH`
<a id="insn-00acb60c"></a> `00acb60c` | `88 00 a0 72` | movk w8,#0x4, LSL #16 | `FALL_THROUGH`
<a id="insn-00acb610"></a> `00acb610` | `13 68 68 b8` | ldr w19,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acb614"></a> `00acb614` | `cf 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb618"></a> `00acb618` | `93 02 00 34` | cbz w19,0x00acb668 | `CONDITIONAL_JUMP`
<a id="insn-00acb61c"></a> `00acb61c` | `08 80 98 52` | mov w8,#0xc400 | `FALL_THROUGH`
<a id="insn-00acb620"></a> `00acb620` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00acb624"></a> `00acb624` | `43 c2 01 94` | bl 0x00b3bf30 | `UNCONDITIONAL_CALL`
<a id="insn-00acb628"></a> `00acb628` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00acb62c"></a> `00acb62c` | `c9 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb630"></a> `00acb630` | `08 74 97 52` | mov w8,#0xbba0 | `FALL_THROUGH`
<a id="insn-00acb634"></a> `00acb634` | `a8 01 a0 72` | movk w8,#0xd, LSL #16 | `FALL_THROUGH`
<a id="insn-00acb638"></a> `00acb638` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00acb63c"></a> `00acb63c` | `ab 05 00 54` | b.lt 0x00acb6f0 | `CONDITIONAL_JUMP`
<a id="insn-00acb640"></a> `00acb640` | `48 e3 8b 52` | mov w8,#0x5f1a | `FALL_THROUGH`
<a id="insn-00acb644"></a> `00acb644` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00acb648"></a> `00acb648` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acb64c"></a> `00acb64c` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00acb650"></a> `00acb650` | `c0 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb654"></a> `00acb654` | `88 e6 8b 52` | mov w8,#0x5f34 | `FALL_THROUGH`
<a id="insn-00acb658"></a> `00acb658` | `09 e2 84 52` | mov w9,#0x2710 | `FALL_THROUGH`
<a id="insn-00acb65c"></a> `00acb65c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acb660"></a> `00acb660` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acb664"></a> `00acb664` | `28 00 00 14` | b 0x00acb704 | `UNCONDITIONAL_JUMP`
<a id="insn-00acb668"></a> `00acb668` | `08 03 95 52` | mov w8,#0xa818 | `FALL_THROUGH`
<a id="insn-00acb66c"></a> `00acb66c` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00acb670"></a> `00acb670` | `88 00 a0 72` | movk w8,#0x4, LSL #16 | `FALL_THROUGH`
<a id="insn-00acb674"></a> `00acb674` | `13 68 28 b8` | str w19,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acb678"></a> `00acb678` | `b6 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb67c"></a> `00acb67c` | `88 ea 8d 52` | mov w8,#0x6f54 | `FALL_THROUGH`
<a id="insn-00acb680"></a> `00acb680` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acb684"></a> `00acb684` | `13 68 28 38` | strb w19,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00acb688"></a> `00acb688` | `b2 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb68c"></a> `00acb68c` | `b1 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb690"></a> `00acb690` | `08 eb 8d 52` | mov w8,#0x6f58 | `FALL_THROUGH`
<a id="insn-00acb694"></a> `00acb694` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acb698"></a> `00acb698` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acb69c"></a> `00acb69c` | `ad 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb6a0"></a> `00acb6a0` | `ac 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb6a4"></a> `00acb6a4` | `88 eb 8d 52` | mov w8,#0x6f5c | `FALL_THROUGH`
<a id="insn-00acb6a8"></a> `00acb6a8` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acb6ac"></a> `00acb6ac` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acb6b0"></a> `00acb6b0` | `a8 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb6b4"></a> `00acb6b4` | `a7 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb6b8"></a> `00acb6b8` | `08 ec 8d 52` | mov w8,#0x6f60 | `FALL_THROUGH`
<a id="insn-00acb6bc"></a> `00acb6bc` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acb6c0"></a> `00acb6c0` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acb6c4"></a> `00acb6c4` | `a3 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb6c8"></a> `00acb6c8` | `a2 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb6cc"></a> `00acb6cc` | `88 ec 8d 52` | mov w8,#0x6f64 | `FALL_THROUGH`
<a id="insn-00acb6d0"></a> `00acb6d0` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acb6d4"></a> `00acb6d4` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acb6d8"></a> `00acb6d8` | `9e 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb6dc"></a> `00acb6dc` | `96 bd e6 97` | bl 0x0047ad34 | `UNCONDITIONAL_CALL`
<a id="insn-00acb6e0"></a> `00acb6e0` | `41 06 80 52` | mov w1,#0x32 | `FALL_THROUGH`
<a id="insn-00acb6e4"></a> `00acb6e4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb6e8"></a> `00acb6e8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acb6ec"></a> `00acb6ec` | `c4 c6 e6 17` | b 0x0047d1fc | `CALL_TERMINATOR`
<a id="insn-00acb6f0"></a> `00acb6f0` | `1f 78 34 b9` | str wzr,[x0, #0x3478] | `FALL_THROUGH`
<a id="insn-00acb6f4"></a> `00acb6f4` | `97 17 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acb6f8"></a> `00acb6f8` | `08 90 86 52` | mov w8,#0x3480 | `FALL_THROUGH`
<a id="insn-00acb6fc"></a> `00acb6fc` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00acb700"></a> `00acb700` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00acb704"></a> `00acb704` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb708"></a> `00acb708` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acb70c"></a> `00acb70c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acb5bc`](#insn-00acb5bc) 範囲 `[['00acb5bc', '00acb5d3']]`
  - `CONDITIONAL_JUMP` [`00acb5d0`](#insn-00acb5d0) → [`00acb604`](#insn-00acb604)
  - `FALL_THROUGH` [`00acb5d0`](#insn-00acb5d0) → [`00acb5d4`](#insn-00acb5d4)
- ブロック [`00acb5d4`](#insn-00acb5d4) 範囲 `[['00acb5d4', '00acb5db']]`
  - `CONDITIONAL_JUMP` [`00acb5d8`](#insn-00acb5d8) → [`00acb5ec`](#insn-00acb5ec)
  - `FALL_THROUGH` [`00acb5d8`](#insn-00acb5d8) → [`00acb5dc`](#insn-00acb5dc)
- ブロック [`00acb5dc`](#insn-00acb5dc) 範囲 `[['00acb5dc', '00acb5df']]`
  - `CONDITIONAL_JUMP` [`00acb5dc`](#insn-00acb5dc) → [`00acb704`](#insn-00acb704)
  - `FALL_THROUGH` [`00acb5dc`](#insn-00acb5dc) → [`00acb5e0`](#insn-00acb5e0)
- ブロック [`00acb5e0`](#insn-00acb5e0) 範囲 `[['00acb5e0', '00acb5eb']]`
  - `UNCONDITIONAL_JUMP` [`00acb5e8`](#insn-00acb5e8) → [`00acb5f4`](#insn-00acb5f4)
- ブロック [`00acb5ec`](#insn-00acb5ec) 範囲 `[['00acb5ec', '00acb5f3']]`
  - `FALL_THROUGH` [`00acb5f0`](#insn-00acb5f0) → [`00acb5f4`](#insn-00acb5f4)
- ブロック [`00acb5f4`](#insn-00acb5f4) 範囲 `[['00acb5f4', '00acb603']]`
- ブロック [`00acb604`](#insn-00acb604) 範囲 `[['00acb604', '00acb61b']]`
  - `CONDITIONAL_JUMP` [`00acb618`](#insn-00acb618) → [`00acb668`](#insn-00acb668)
  - `FALL_THROUGH` [`00acb618`](#insn-00acb618) → [`00acb61c`](#insn-00acb61c)
- ブロック [`00acb61c`](#insn-00acb61c) 範囲 `[['00acb61c', '00acb63f']]`
  - `CONDITIONAL_JUMP` [`00acb63c`](#insn-00acb63c) → [`00acb6f0`](#insn-00acb6f0)
  - `FALL_THROUGH` [`00acb63c`](#insn-00acb63c) → [`00acb640`](#insn-00acb640)
- ブロック [`00acb640`](#insn-00acb640) 範囲 `[['00acb640', '00acb667']]`
  - `UNCONDITIONAL_JUMP` [`00acb664`](#insn-00acb664) → [`00acb704`](#insn-00acb704)
- ブロック [`00acb668`](#insn-00acb668) 範囲 `[['00acb668', '00acb6ef']]`
- ブロック [`00acb6f0`](#insn-00acb6f0) 範囲 `[['00acb6f0', '00acb703']]`
  - `FALL_THROUGH` [`00acb700`](#insn-00acb700) → [`00acb704`](#insn-00acb704)
- ブロック [`00acb704`](#insn-00acb704) 範囲 `[['00acb704', '00acb70f']]`

## 命令位置別の参照

- [`00acb5bc`](#insn-00acb5bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5c0`](#insn-00acb5c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5d0`](#insn-00acb5d0) → [`00acb604`](#insn-00acb604) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5d8`](#insn-00acb5d8) → [`00acb5ec`](#insn-00acb5ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5dc`](#insn-00acb5dc) → [`00acb704`](#insn-00acb704) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5e0`](#insn-00acb5e0) → [`0047ad34`](../0047a/0047ad34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ad34` · 推定シンボル `None` · 推定型 `None`
- [`00acb5e8`](#insn-00acb5e8) → [`00acb5f4`](#insn-00acb5f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5ec`](#insn-00acb5ec) → [`0047ad34`](../0047a/0047ad34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ad34` · 推定シンボル `None` · 推定型 `None`
- [`00acb5f8`](#insn-00acb5f8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5fc`](#insn-00acb5fc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb600`](#insn-00acb600) → [`0047ce14`](../0047c/0047ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ce14` · 推定シンボル `None` · 推定型 `None`
- [`00acb604`](#insn-00acb604) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb614`](#insn-00acb614) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb618`](#insn-00acb618) → [`00acb668`](#insn-00acb668) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb624`](#insn-00acb624) → [`00b3bf30`](../00b3b/00b3bf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3bf30` · 推定シンボル `None` · 推定型 `None`
- [`00acb62c`](#insn-00acb62c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb63c`](#insn-00acb63c) → [`00acb6f0`](#insn-00acb6f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb64c`](#insn-00acb64c) → `00335f1a`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acb650`](#insn-00acb650) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb660`](#insn-00acb660) → `00335f34`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acb664`](#insn-00acb664) → [`00acb704`](#insn-00acb704) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb678`](#insn-00acb678) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb684`](#insn-00acb684) → `00336f54`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acb688`](#insn-00acb688) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb68c`](#insn-00acb68c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb698`](#insn-00acb698) → `00336f58`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acb69c`](#insn-00acb69c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb6a0`](#insn-00acb6a0) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb6ac`](#insn-00acb6ac) → `00336f5c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acb6b0`](#insn-00acb6b0) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb6b4`](#insn-00acb6b4) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb6c0`](#insn-00acb6c0) → `00336f60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acb6c4`](#insn-00acb6c4) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb6c8`](#insn-00acb6c8) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb6d4`](#insn-00acb6d4) → `00336f64`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acb6d8`](#insn-00acb6d8) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb6dc`](#insn-00acb6dc) → [`0047ad34`](../0047a/0047ad34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ad34` · 推定シンボル `None` · 推定型 `None`
- [`00acb6e4`](#insn-00acb6e4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6e8`](#insn-00acb6e8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6ec`](#insn-00acb6ec) → [`0047d1fc`](../0047d/0047d1fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047d1fc` · 推定シンボル `None` · 推定型 `None`
- [`00acb6f4`](#insn-00acb6f4) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acb704`](#insn-00acb704) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb708`](#insn-00acb708) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acb5bc`](#insn-00acb5bc)

~~~json
{
  "source": "00acb5bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5c0`](#insn-00acb5c0)

~~~json
{
  "source": "00acb5c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5d0`](#insn-00acb5d0)

~~~json
{
  "source": "00acb5d0",
  "target": "00acb604",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5d8`](#insn-00acb5d8)

~~~json
{
  "source": "00acb5d8",
  "target": "00acb5ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5dc`](#insn-00acb5dc)

~~~json
{
  "source": "00acb5dc",
  "target": "00acb704",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5e0`](#insn-00acb5e0)

~~~json
{
  "source": "00acb5e0",
  "target": "0047ad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb5e8`](#insn-00acb5e8)

~~~json
{
  "source": "00acb5e8",
  "target": "00acb5f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5ec`](#insn-00acb5ec)

~~~json
{
  "source": "00acb5ec",
  "target": "0047ad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb5f8`](#insn-00acb5f8)

~~~json
{
  "source": "00acb5f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5fc`](#insn-00acb5fc)

~~~json
{
  "source": "00acb5fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb600`](#insn-00acb600)

~~~json
{
  "source": "00acb600",
  "target": "0047ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb604`](#insn-00acb604)

~~~json
{
  "source": "00acb604",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb614`](#insn-00acb614)

~~~json
{
  "source": "00acb614",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb618`](#insn-00acb618)

~~~json
{
  "source": "00acb618",
  "target": "00acb668",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb624`](#insn-00acb624)

~~~json
{
  "source": "00acb624",
  "target": "00b3bf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb62c`](#insn-00acb62c)

~~~json
{
  "source": "00acb62c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb63c`](#insn-00acb63c)

~~~json
{
  "source": "00acb63c",
  "target": "00acb6f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb64c`](#insn-00acb64c)

~~~json
{
  "source": "00acb64c",
  "target": "00335f1a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335f18",
  "offset": 2,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "446b750074fd0900",
  "capture_start": "00335f18",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acb650`](#insn-00acb650)

~~~json
{
  "source": "00acb650",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb660`](#insn-00acb660)

~~~json
{
  "source": "00acb660",
  "target": "00335f34",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335f30",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "9c6b7500c4fd0900",
  "capture_start": "00335f30",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acb664`](#insn-00acb664)

~~~json
{
  "source": "00acb664",
  "target": "00acb704",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb678`](#insn-00acb678)

~~~json
{
  "source": "00acb678",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb684`](#insn-00acb684)

~~~json
{
  "source": "00acb684",
  "target": "00336f54",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00336f50",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "2472780038330a00",
  "capture_start": "00336f50",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acb688`](#insn-00acb688)

~~~json
{
  "source": "00acb688",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb68c`](#insn-00acb68c)

~~~json
{
  "source": "00acb68c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb698`](#insn-00acb698)

~~~json
{
  "source": "00acb698",
  "target": "00336f58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00336f58",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "387278004c330a00",
  "capture_start": "00336f58",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acb69c`](#insn-00acb69c)

~~~json
{
  "source": "00acb69c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb6a0`](#insn-00acb6a0)

~~~json
{
  "source": "00acb6a0",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb6ac`](#insn-00acb6ac)

~~~json
{
  "source": "00acb6ac",
  "target": "00336f5c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00336f58",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "387278004c330a00",
  "capture_start": "00336f58",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acb6b0`](#insn-00acb6b0)

~~~json
{
  "source": "00acb6b0",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb6b4`](#insn-00acb6b4)

~~~json
{
  "source": "00acb6b4",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb6c0`](#insn-00acb6c0)

~~~json
{
  "source": "00acb6c0",
  "target": "00336f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00336f60",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "3c72780060330a00",
  "capture_start": "00336f60",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acb6c4`](#insn-00acb6c4)

~~~json
{
  "source": "00acb6c4",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb6c8`](#insn-00acb6c8)

~~~json
{
  "source": "00acb6c8",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb6d4`](#insn-00acb6d4)

~~~json
{
  "source": "00acb6d4",
  "target": "00336f64",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00336f60",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "3c72780060330a00",
  "capture_start": "00336f60",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acb6d8`](#insn-00acb6d8)

~~~json
{
  "source": "00acb6d8",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb6dc`](#insn-00acb6dc)

~~~json
{
  "source": "00acb6dc",
  "target": "0047ad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb6e4`](#insn-00acb6e4)

~~~json
{
  "source": "00acb6e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6e8`](#insn-00acb6e8)

~~~json
{
  "source": "00acb6e8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6ec`](#insn-00acb6ec)

~~~json
{
  "source": "00acb6ec",
  "target": "0047d1fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb6f4`](#insn-00acb6f4)

~~~json
{
  "source": "00acb6f4",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb704`](#insn-00acb704)

~~~json
{
  "source": "00acb704",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb708`](#insn-00acb708)

~~~json
{
  "source": "00acb708",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
