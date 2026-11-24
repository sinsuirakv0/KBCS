# 00bfaaa0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf9aac`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9aac.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-43f74062764d7bc20437fd90b0ee5a1a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaaa0",
  "name": "_ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dbd1d9ab0bd02154146a73b796c31062cd3920d51f86cdc185027ab5c2ce3b67",
  "source_text_sha256": "dbd1d9ab0bd02154146a73b796c31062cd3920d51f86cdc185027ab5c2ce3b67",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfaaa0",
        "00bfab2f"
      ]
    ],
    "bytes_sha256": "b4825163949c63291511e352a0b66475cfbf42e6135edfb3e5800d99b1857115",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c59540](../00c59/00c59540.md)

## 呼び出し先

- [00c59190](../00c59/00c59190.md)
- [00c591c0](../00c59/00c591c0.md)
- [00c59520](../00c59/00c59520.md)

## 関連文字列（未確認候補）

~~~text
"unique_lock::unlock: not locked"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1079 bytes

~~~c

void _ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE
               (long *param_1,undefined8 *param_2)

{
  uint uVar1;
  byte bVar2;
  long lVar3;
  
  uVar1 = *(uint *)(param_1 + 0xe);
  if ((uVar1 >> 2 & 1) == 0) {
    if ((uVar1 >> 3 & 1) != 0) {
      bVar2 = *(byte *)(param_2 + 1);
      *(uint *)(param_1 + 0xe) = uVar1 & 0xfffffff3;
      if ((bVar2 & 1) != 0) {
        _ZNSt6__ndk15mutex6unlockEv(*param_2);
        lVar3 = *param_1;
        *(undefined1 *)(param_2 + 1) = 0;
                    /* WARNING: Could not recover jumptable at 0x00bfab1c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
        (**(code **)(lVar3 + 0x18))(param_1);
        return;
      }
                    /* WARNING: Subroutine does not return */
      _ZNSt6__ndk120__throw_system_errorEiPKc(1,"unique_lock::unlock: not locked");
    }
    do {
      _ZNSt6__ndk118condition_variable4waitERNS_11unique_lockINS_5mutexEEE(param_1 + 8,param_2);
    } while ((*(byte *)(param_1 + 0xe) >> 2 & 1) == 0);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfaaa0"></a> `00bfaaa0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfaaa4"></a> `00bfaaa4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfaaa8"></a> `00bfaaa8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfaaac"></a> `00bfaaac` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfaab0"></a> `00bfaab0` | `08 70 40 b9` | ldr w8,[x0, #0x70] | `FALL_THROUGH`
<a id="insn-00bfaab4"></a> `00bfaab4` | `28 01 10 37` | tbnz w8,#0x2,0x00bfaad8 | `CONDITIONAL_JUMP`
<a id="insn-00bfaab8"></a> `00bfaab8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfaabc"></a> `00bfaabc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfaac0"></a> `00bfaac0` | `48 01 18 37` | tbnz w8,#0x3,0x00bfaae8 | `CONDITIONAL_JUMP`
<a id="insn-00bfaac4"></a> `00bfaac4` | `60 02 01 91` | add x0,x19,#0x40 | `FALL_THROUGH`
<a id="insn-00bfaac8"></a> `00bfaac8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bfaacc"></a> `00bfaacc` | `95 7a 01 94` | bl 0x00c59520 | `UNCONDITIONAL_CALL`
<a id="insn-00bfaad0"></a> `00bfaad0` | `68 c2 41 39` | ldrb w8,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00bfaad4"></a> `00bfaad4` | `88 ff 17 36` | tbz w8,#0x2,0x00bfaac4 | `CONDITIONAL_JUMP`
<a id="insn-00bfaad8"></a> `00bfaad8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfaadc"></a> `00bfaadc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfaae0"></a> `00bfaae0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfaae4"></a> `00bfaae4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfaae8"></a> `00bfaae8` | `89 22 40 39` | ldrb w9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bfaaec"></a> `00bfaaec` | `08 75 1c 12` | and w8,w8,#0xfffffff3 | `FALL_THROUGH`
<a id="insn-00bfaaf0"></a> `00bfaaf0` | `68 72 00 b9` | str w8,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00bfaaf4"></a> `00bfaaf4` | `69 01 00 36` | tbz w9,#0x0,0x00bfab20 | `CONDITIONAL_JUMP`
<a id="insn-00bfaaf8"></a> `00bfaaf8` | `80 02 40 f9` | ldr x0,[x20] | `FALL_THROUGH`
<a id="insn-00bfaafc"></a> `00bfaafc` | `a5 79 01 94` | bl 0x00c59190 | `UNCONDITIONAL_CALL`
<a id="insn-00bfab00"></a> `00bfab00` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfab04"></a> `00bfab04` | `9f 22 00 39` | strb wzr,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bfab08"></a> `00bfab08` | `10 0d 40 f9` | ldr x16,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bfab0c"></a> `00bfab0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfab10"></a> `00bfab10` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfab14"></a> `00bfab14` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfab18"></a> `00bfab18` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfab1c"></a> `00bfab1c` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bfab20"></a> `00bfab20` | `21 b6 ff 90` | adrp x1,0x2be000 | `FALL_THROUGH`
<a id="insn-00bfab24"></a> `00bfab24` | `21 94 2a 91` | add x1,x1,#0xaa5 | `FALL_THROUGH`
<a id="insn-00bfab28"></a> `00bfab28` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfab2c"></a> `00bfab2c` | `a5 79 01 94` | bl 0x00c591c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfaaa0`](#insn-00bfaaa0) 範囲 `[['00bfaaa0', '00bfaab7']]`
  - `CONDITIONAL_JUMP` [`00bfaab4`](#insn-00bfaab4) → [`00bfaad8`](#insn-00bfaad8)
  - `FALL_THROUGH` [`00bfaab4`](#insn-00bfaab4) → [`00bfaab8`](#insn-00bfaab8)
- ブロック [`00bfaab8`](#insn-00bfaab8) 範囲 `[['00bfaab8', '00bfaac3']]`
  - `CONDITIONAL_JUMP` [`00bfaac0`](#insn-00bfaac0) → [`00bfaae8`](#insn-00bfaae8)
  - `FALL_THROUGH` [`00bfaac0`](#insn-00bfaac0) → [`00bfaac4`](#insn-00bfaac4)
- ブロック [`00bfaac4`](#insn-00bfaac4) 範囲 `[['00bfaac4', '00bfaad7']]`
  - `CONDITIONAL_JUMP` [`00bfaad4`](#insn-00bfaad4) → [`00bfaac4`](#insn-00bfaac4)
  - `FALL_THROUGH` [`00bfaad4`](#insn-00bfaad4) → [`00bfaad8`](#insn-00bfaad8)
- ブロック [`00bfaad8`](#insn-00bfaad8) 範囲 `[['00bfaad8', '00bfaae7']]`
- ブロック [`00bfaae8`](#insn-00bfaae8) 範囲 `[['00bfaae8', '00bfaaf7']]`
  - `CONDITIONAL_JUMP` [`00bfaaf4`](#insn-00bfaaf4) → [`00bfab20`](#insn-00bfab20)
  - `FALL_THROUGH` [`00bfaaf4`](#insn-00bfaaf4) → [`00bfaaf8`](#insn-00bfaaf8)
- ブロック [`00bfaaf8`](#insn-00bfaaf8) 範囲 `[['00bfaaf8', '00bfab1f']]`
- ブロック [`00bfab20`](#insn-00bfab20) 範囲 `[['00bfab20', '00bfab2f']]`

## 命令位置別の参照

- [`00bfaaa4`](#insn-00bfaaa4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaaa8`](#insn-00bfaaa8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaab4`](#insn-00bfaab4) → [`00bfaad8`](#insn-00bfaad8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaac0`](#insn-00bfaac0) → [`00bfaae8`](#insn-00bfaae8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaacc`](#insn-00bfaacc) → [`00c59520`](../00c59/00c59520.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59520` · 推定シンボル `None` · 推定型 `None`
- [`00bfaad4`](#insn-00bfaad4) → [`00bfaac4`](#insn-00bfaac4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaad8`](#insn-00bfaad8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaadc`](#insn-00bfaadc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaaf4`](#insn-00bfaaf4) → [`00bfab20`](#insn-00bfab20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaafc`](#insn-00bfaafc) → [`00c59190`](../00c59/00c59190.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59190` · 推定シンボル `None` · 推定型 `None`
- [`00bfab10`](#insn-00bfab10) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfab14`](#insn-00bfab14) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfab24`](#insn-00bfab24) → `002beaa5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfab2c`](#insn-00bfab2c) → [`00c591c0`](../00c59/00c591c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c591c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfaaa4`](#insn-00bfaaa4)

~~~json
{
  "source": "00bfaaa4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaaa8`](#insn-00bfaaa8)

~~~json
{
  "source": "00bfaaa8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaab4`](#insn-00bfaab4)

~~~json
{
  "source": "00bfaab4",
  "target": "00bfaad8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaac0`](#insn-00bfaac0)

~~~json
{
  "source": "00bfaac0",
  "target": "00bfaae8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaacc`](#insn-00bfaacc)

~~~json
{
  "source": "00bfaacc",
  "target": "00c59520",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfaad4`](#insn-00bfaad4)

~~~json
{
  "source": "00bfaad4",
  "target": "00bfaac4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaad8`](#insn-00bfaad8)

~~~json
{
  "source": "00bfaad8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaadc`](#insn-00bfaadc)

~~~json
{
  "source": "00bfaadc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaaf4`](#insn-00bfaaf4)

~~~json
{
  "source": "00bfaaf4",
  "target": "00bfab20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaafc`](#insn-00bfaafc)

~~~json
{
  "source": "00bfaafc",
  "target": "00c59190",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfab10`](#insn-00bfab10)

~~~json
{
  "source": "00bfab10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfab14`](#insn-00bfab14)

~~~json
{
  "source": "00bfab14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfab24`](#insn-00bfab24)

~~~json
{
  "source": "00bfab24",
  "target": "002beaa5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002beaa5",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "756e697175655f6c6f636b3a3a756e6c6f636b3a206e6f74206c6f636b656400",
  "capture_start": "002beaa5",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfab2c`](#insn-00bfab2c)

~~~json
{
  "source": "00bfab2c",
  "target": "00c591c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
