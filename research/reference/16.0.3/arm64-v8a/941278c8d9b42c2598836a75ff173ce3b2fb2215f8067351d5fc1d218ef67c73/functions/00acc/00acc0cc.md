# 00acc0cc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acb0d8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb0d8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0028.md#compare-4529729a05cb44f48f835aebce58e1be)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acc0cc",
  "name": "FUN_00acc0cc",
  "size": 356,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6bfd39b82dcfdb05ccc1ac17e8ab1edab10666525c6ffa9a9ea0ce240451bf58",
  "source_text_sha256": "6bfd39b82dcfdb05ccc1ac17e8ab1edab10666525c6ffa9a9ea0ce240451bf58",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acc0cc",
        "00acc22f"
      ]
    ],
    "bytes_sha256": "2d859a262395f04004639d067838d16d5fea589596e59286c859c8ad1a38d4a0",
    "instruction_count": 89,
    "instruction_bytes": 356,
    "body_bytes": 356,
    "indirect": 10,
    "unresolved": 10
  }
}
~~~

## 呼び出し元

- [00ac9a0c](../00ac9/00ac9a0c.md)
- [00aca49c](../00aca/00aca49c.md)

## 呼び出し先

- [00c58f80](../00c58/00c58f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1450 bytes

~~~c

void FUN_00acc0cc(long *param_1,long *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long local_60 [5];
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if (param_2 != param_1) {
    plVar2 = (long *)param_1[4];
    plVar3 = (long *)param_2[4];
    if (plVar2 == param_1) {
      if (plVar3 == param_2) {
        (**(code **)(*param_1 + 0x18))(param_1,local_60);
        (**(code **)(*(long *)param_1[4] + 0x20))();
        param_1[4] = 0;
        (**(code **)(*(long *)param_2[4] + 0x18))((long *)param_2[4],param_1);
        (**(code **)(*(long *)param_2[4] + 0x20))();
        param_2[4] = 0;
        param_1[4] = (long)param_1;
        (**(code **)(local_60[0] + 0x18))(local_60,param_2);
        (**(code **)(local_60[0] + 0x20))(local_60);
      }
      else {
        (**(code **)(*param_1 + 0x18))(param_1,param_2);
        (**(code **)(*(long *)param_1[4] + 0x20))();
        param_1[4] = param_2[4];
      }
      param_2[4] = (long)param_2;
    }
    else if (plVar3 == param_2) {
      (**(code **)(*param_2 + 0x18))(param_2,param_1);
      (**(code **)(*(long *)param_2[4] + 0x20))();
      param_2[4] = param_1[4];
      param_1[4] = (long)param_1;
    }
    else {
      param_1[4] = (long)plVar3;
      param_2[4] = (long)plVar2;
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
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
<a id="insn-00acc0cc"></a> `00acc0cc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acc0d0"></a> `00acc0d0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acc0d4"></a> `00acc0d4` | `f5 23 00 f9` | str x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acc0d8"></a> `00acc0d8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acc0dc"></a> `00acc0dc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00acc0e0"></a> `00acc0e0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acc0e4"></a> `00acc0e4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acc0e8"></a> `00acc0e8` | `3f 00 00 eb` | cmp x1,x0 | `FALL_THROUGH`
<a id="insn-00acc0ec"></a> `00acc0ec` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acc0f0"></a> `00acc0f0` | `c0 08 00 54` | b.eq 0x00acc208 | `CONDITIONAL_JUMP`
<a id="insn-00acc0f4"></a> `00acc0f4` | `08 10 40 f9` | ldr x8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00acc0f8"></a> `00acc0f8` | `29 10 40 f9` | ldr x9,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00acc0fc"></a> `00acc0fc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00acc100"></a> `00acc100` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acc104"></a> `00acc104` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00acc108"></a> `00acc108` | `c0 00 00 54` | b.eq 0x00acc120 | `CONDITIONAL_JUMP`
<a id="insn-00acc10c"></a> `00acc10c` | `3f 01 13 eb` | cmp x9,x19 | `FALL_THROUGH`
<a id="insn-00acc110"></a> `00acc110` | `40 02 00 54` | b.eq 0x00acc158 | `CONDITIONAL_JUMP`
<a id="insn-00acc114"></a> `00acc114` | `89 12 00 f9` | str x9,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acc118"></a> `00acc118` | `68 12 00 f9` | str x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acc11c"></a> `00acc11c` | `3b 00 00 14` | b 0x00acc208 | `UNCONDITIONAL_JUMP`
<a id="insn-00acc120"></a> `00acc120` | `3f 01 13 eb` | cmp x9,x19 | `FALL_THROUGH`
<a id="insn-00acc124"></a> `00acc124` | `40 03 00 54` | b.eq 0x00acc18c | `CONDITIONAL_JUMP`
<a id="insn-00acc128"></a> `00acc128` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acc12c"></a> `00acc12c` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acc130"></a> `00acc130` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acc134"></a> `00acc134` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acc138"></a> `00acc138` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acc13c"></a> `00acc13c` | `80 12 40 f9` | ldr x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acc140"></a> `00acc140` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acc144"></a> `00acc144` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00acc148"></a> `00acc148` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acc14c"></a> `00acc14c` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acc150"></a> `00acc150` | `88 12 00 f9` | str x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acc154"></a> `00acc154` | `2c 00 00 14` | b 0x00acc204 | `UNCONDITIONAL_JUMP`
<a id="insn-00acc158"></a> `00acc158` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acc15c"></a> `00acc15c` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acc160"></a> `00acc160` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acc164"></a> `00acc164` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00acc168"></a> `00acc168` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acc16c"></a> `00acc16c` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acc170"></a> `00acc170` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acc174"></a> `00acc174` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00acc178"></a> `00acc178` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acc17c"></a> `00acc17c` | `88 12 40 f9` | ldr x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acc180"></a> `00acc180` | `68 12 00 f9` | str x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acc184"></a> `00acc184` | `94 12 00 f9` | str x20,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acc188"></a> `00acc188` | `20 00 00 14` | b 0x00acc208 | `UNCONDITIONAL_JUMP`
<a id="insn-00acc18c"></a> `00acc18c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acc190"></a> `00acc190` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acc194"></a> `00acc194` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00acc198"></a> `00acc198` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acc19c"></a> `00acc19c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acc1a0"></a> `00acc1a0` | `80 12 40 f9` | ldr x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acc1a4"></a> `00acc1a4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acc1a8"></a> `00acc1a8` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00acc1ac"></a> `00acc1ac` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acc1b0"></a> `00acc1b0` | `9f 12 00 f9` | str xzr,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acc1b4"></a> `00acc1b4` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acc1b8"></a> `00acc1b8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acc1bc"></a> `00acc1bc` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acc1c0"></a> `00acc1c0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00acc1c4"></a> `00acc1c4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acc1c8"></a> `00acc1c8` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acc1cc"></a> `00acc1cc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acc1d0"></a> `00acc1d0` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00acc1d4"></a> `00acc1d4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acc1d8"></a> `00acc1d8` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00acc1dc"></a> `00acc1dc` | `7f 12 00 f9` | str xzr,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acc1e0"></a> `00acc1e0` | `94 12 00 f9` | str x20,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acc1e4"></a> `00acc1e4` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acc1e8"></a> `00acc1e8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acc1ec"></a> `00acc1ec` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acc1f0"></a> `00acc1f0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acc1f4"></a> `00acc1f4` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00acc1f8"></a> `00acc1f8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acc1fc"></a> `00acc1fc` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00acc200"></a> `00acc200` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acc204"></a> `00acc204` | `73 12 00 f9` | str x19,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acc208"></a> `00acc208` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acc20c"></a> `00acc20c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acc210"></a> `00acc210` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acc214"></a> `00acc214` | `c1 00 00 54` | b.ne 0x00acc22c | `CONDITIONAL_JUMP`
<a id="insn-00acc218"></a> `00acc218` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acc21c"></a> `00acc21c` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acc220"></a> `00acc220` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acc224"></a> `00acc224` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acc228"></a> `00acc228` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acc22c"></a> `00acc22c` | `55 33 06 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acc0cc`](#insn-00acc0cc) 範囲 `[['00acc0cc', '00acc0f3']]`
  - `CONDITIONAL_JUMP` [`00acc0f0`](#insn-00acc0f0) → [`00acc208`](#insn-00acc208)
  - `FALL_THROUGH` [`00acc0f0`](#insn-00acc0f0) → [`00acc0f4`](#insn-00acc0f4)
- ブロック [`00acc0f4`](#insn-00acc0f4) 範囲 `[['00acc0f4', '00acc10b']]`
  - `CONDITIONAL_JUMP` [`00acc108`](#insn-00acc108) → [`00acc120`](#insn-00acc120)
  - `FALL_THROUGH` [`00acc108`](#insn-00acc108) → [`00acc10c`](#insn-00acc10c)
- ブロック [`00acc10c`](#insn-00acc10c) 範囲 `[['00acc10c', '00acc113']]`
  - `CONDITIONAL_JUMP` [`00acc110`](#insn-00acc110) → [`00acc158`](#insn-00acc158)
  - `FALL_THROUGH` [`00acc110`](#insn-00acc110) → [`00acc114`](#insn-00acc114)
- ブロック [`00acc114`](#insn-00acc114) 範囲 `[['00acc114', '00acc11f']]`
  - `UNCONDITIONAL_JUMP` [`00acc11c`](#insn-00acc11c) → [`00acc208`](#insn-00acc208)
- ブロック [`00acc120`](#insn-00acc120) 範囲 `[['00acc120', '00acc127']]`
  - `CONDITIONAL_JUMP` [`00acc124`](#insn-00acc124) → [`00acc18c`](#insn-00acc18c)
  - `FALL_THROUGH` [`00acc124`](#insn-00acc124) → [`00acc128`](#insn-00acc128)
- ブロック [`00acc128`](#insn-00acc128) 範囲 `[['00acc128', '00acc157']]`
  - `UNCONDITIONAL_JUMP` [`00acc154`](#insn-00acc154) → [`00acc204`](#insn-00acc204)
- ブロック [`00acc158`](#insn-00acc158) 範囲 `[['00acc158', '00acc18b']]`
  - `UNCONDITIONAL_JUMP` [`00acc188`](#insn-00acc188) → [`00acc208`](#insn-00acc208)
- ブロック [`00acc18c`](#insn-00acc18c) 範囲 `[['00acc18c', '00acc203']]`
  - `FALL_THROUGH` [`00acc200`](#insn-00acc200) → [`00acc204`](#insn-00acc204)
- ブロック [`00acc204`](#insn-00acc204) 範囲 `[['00acc204', '00acc207']]`
  - `FALL_THROUGH` [`00acc204`](#insn-00acc204) → [`00acc208`](#insn-00acc208)
- ブロック [`00acc208`](#insn-00acc208) 範囲 `[['00acc208', '00acc217']]`
  - `CONDITIONAL_JUMP` [`00acc214`](#insn-00acc214) → [`00acc22c`](#insn-00acc22c)
  - `FALL_THROUGH` [`00acc214`](#insn-00acc214) → [`00acc218`](#insn-00acc218)
- ブロック [`00acc218`](#insn-00acc218) 範囲 `[['00acc218', '00acc22b']]`
- ブロック [`00acc22c`](#insn-00acc22c) 範囲 `[['00acc22c', '00acc22f']]`

## 命令位置別の参照

- [`00acc0d0`](#insn-00acc0d0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc0d4`](#insn-00acc0d4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc0d8`](#insn-00acc0d8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc0ec`](#insn-00acc0ec) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc0f0`](#insn-00acc0f0) → [`00acc208`](#insn-00acc208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc108`](#insn-00acc108) → [`00acc120`](#insn-00acc120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc110`](#insn-00acc110) → [`00acc158`](#insn-00acc158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc11c`](#insn-00acc11c) → [`00acc208`](#insn-00acc208) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc124`](#insn-00acc124) → [`00acc18c`](#insn-00acc18c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc154`](#insn-00acc154) → [`00acc204`](#insn-00acc204) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc188`](#insn-00acc188) → [`00acc208`](#insn-00acc208) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc1d8`](#insn-00acc1d8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc1f4`](#insn-00acc1f4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc20c`](#insn-00acc20c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc214`](#insn-00acc214) → [`00acc22c`](#insn-00acc22c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc218`](#insn-00acc218) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc21c`](#insn-00acc21c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc220`](#insn-00acc220) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc22c`](#insn-00acc22c) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acc0d0`](#insn-00acc0d0)

~~~json
{
  "source": "00acc0d0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc0d4`](#insn-00acc0d4)

~~~json
{
  "source": "00acc0d4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc0d8`](#insn-00acc0d8)

~~~json
{
  "source": "00acc0d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc0ec`](#insn-00acc0ec)

~~~json
{
  "source": "00acc0ec",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc0f0`](#insn-00acc0f0)

~~~json
{
  "source": "00acc0f0",
  "target": "00acc208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc108`](#insn-00acc108)

~~~json
{
  "source": "00acc108",
  "target": "00acc120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc110`](#insn-00acc110)

~~~json
{
  "source": "00acc110",
  "target": "00acc158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc11c`](#insn-00acc11c)

~~~json
{
  "source": "00acc11c",
  "target": "00acc208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc124`](#insn-00acc124)

~~~json
{
  "source": "00acc124",
  "target": "00acc18c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc154`](#insn-00acc154)

~~~json
{
  "source": "00acc154",
  "target": "00acc204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc188`](#insn-00acc188)

~~~json
{
  "source": "00acc188",
  "target": "00acc208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc1d8`](#insn-00acc1d8)

~~~json
{
  "source": "00acc1d8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc1f4`](#insn-00acc1f4)

~~~json
{
  "source": "00acc1f4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc20c`](#insn-00acc20c)

~~~json
{
  "source": "00acc20c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc214`](#insn-00acc214)

~~~json
{
  "source": "00acc214",
  "target": "00acc22c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc218`](#insn-00acc218)

~~~json
{
  "source": "00acc218",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc21c`](#insn-00acc21c)

~~~json
{
  "source": "00acc21c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc220`](#insn-00acc220)

~~~json
{
  "source": "00acc220",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc22c`](#insn-00acc22c)

~~~json
{
  "source": "00acc22c",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
