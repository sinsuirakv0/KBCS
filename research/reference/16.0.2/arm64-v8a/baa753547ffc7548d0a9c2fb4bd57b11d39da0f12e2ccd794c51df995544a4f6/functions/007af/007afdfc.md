# 007afdfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `007afda4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afda4.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0039.md#compare-b3b56312708addbe3fc180d4dc56366a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `007b0820`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007b0/007b0820.md) · 移動量 `+0xa24`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0040.md#compare-787a197da32ec15567785246c8095ab6)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007afdfc",
  "name": "FUN_007afdfc",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7286e3d23c654116de47a8757eaed5fc3848315a8def3554ac676bb819afc091",
  "source_text_sha256": "7286e3d23c654116de47a8757eaed5fc3848315a8def3554ac676bb819afc091",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007afdfc",
        "007afe6f"
      ]
    ],
    "bytes_sha256": "c727afac3c08e09b0bc65a1406b16d930cb791044075fc6ee019df8fea33f8ca",
    "instruction_count": 29,
    "instruction_bytes": 116,
    "body_bytes": 116,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 641 bytes

~~~c

void FUN_007afdfc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  long *plVar2;
  
  plVar2 = *(long **)(param_1 + 0x30);
  *param_2 = &PTR_FUN_00c7aae8;
  if (plVar2 == (long *)0x0) {
    param_2[6] = 0;
  }
  else {
    if (plVar2 == (long *)(param_1 + 0x10)) {
      param_2[6] = param_2 + 2;
                    /* WARNING: Could not recover jumptable at 0x007afe6c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(**(long **)(param_1 + 0x30) + 0x18))();
      return;
    }
    uVar1 = (**(code **)(*plVar2 + 0x10))(plVar2);
    param_2[6] = uVar1;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007afdfc"></a> `007afdfc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007afe00"></a> `007afe00` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007afe04"></a> `007afe04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007afe08"></a> `007afe08` | `08 18 40 f9` | ldr x8,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-007afe0c"></a> `007afe0c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-007afe10"></a> `007afe10` | `49 26 00 f0` | adrp x9,0xc7a000 | `FALL_THROUGH`
<a id="insn-007afe14"></a> `007afe14` | `29 a1 2b 91` | add x9,x9,#0xae8 | `FALL_THROUGH`
<a id="insn-007afe18"></a> `007afe18` | `29 04 01 f8` | str x9,[x1], #0x10 | `FALL_THROUGH`
<a id="insn-007afe1c"></a> `007afe1c` | `48 01 00 b4` | cbz x8,0x007afe44 | `CONDITIONAL_JUMP`
<a id="insn-007afe20"></a> `007afe20` | `09 40 00 91` | add x9,x0,#0x10 | `FALL_THROUGH`
<a id="insn-007afe24"></a> `007afe24` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-007afe28"></a> `007afe28` | `60 01 00 54` | b.eq 0x007afe54 | `CONDITIONAL_JUMP`
<a id="insn-007afe2c"></a> `007afe2c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-007afe30"></a> `007afe30` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-007afe34"></a> `007afe34` | `29 09 40 f9` | ldr x9,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-007afe38"></a> `007afe38` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-007afe3c"></a> `007afe3c` | `60 1a 00 f9` | str x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-007afe40"></a> `007afe40` | `02 00 00 14` | b 0x007afe48 | `UNCONDITIONAL_JUMP`
<a id="insn-007afe44"></a> `007afe44` | `7f 1a 00 f9` | str xzr,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-007afe48"></a> `007afe48` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007afe4c"></a> `007afe4c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007afe50"></a> `007afe50` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007afe54"></a> `007afe54` | `61 1a 00 f9` | str x1,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-007afe58"></a> `007afe58` | `00 18 40 f9` | ldr x0,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-007afe5c"></a> `007afe5c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-007afe60"></a> `007afe60` | `02 0d 40 f9` | ldr x2,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-007afe64"></a> `007afe64` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007afe68"></a> `007afe68` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007afe6c"></a> `007afe6c` | `40 00 1f d6` | br x2 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`007afdfc`](#insn-007afdfc) 範囲 `[['007afdfc', '007afe1f']]`
  - `CONDITIONAL_JUMP` [`007afe1c`](#insn-007afe1c) → [`007afe44`](#insn-007afe44)
  - `FALL_THROUGH` [`007afe1c`](#insn-007afe1c) → [`007afe20`](#insn-007afe20)
- ブロック [`007afe20`](#insn-007afe20) 範囲 `[['007afe20', '007afe2b']]`
  - `CONDITIONAL_JUMP` [`007afe28`](#insn-007afe28) → [`007afe54`](#insn-007afe54)
  - `FALL_THROUGH` [`007afe28`](#insn-007afe28) → [`007afe2c`](#insn-007afe2c)
- ブロック [`007afe2c`](#insn-007afe2c) 範囲 `[['007afe2c', '007afe43']]`
  - `UNCONDITIONAL_JUMP` [`007afe40`](#insn-007afe40) → [`007afe48`](#insn-007afe48)
- ブロック [`007afe44`](#insn-007afe44) 範囲 `[['007afe44', '007afe47']]`
  - `FALL_THROUGH` [`007afe44`](#insn-007afe44) → [`007afe48`](#insn-007afe48)
- ブロック [`007afe48`](#insn-007afe48) 範囲 `[['007afe48', '007afe53']]`
- ブロック [`007afe54`](#insn-007afe54) 範囲 `[['007afe54', '007afe6f']]`

## 命令位置別の参照

- [`007afdfc`](#insn-007afdfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afe00`](#insn-007afe00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afe18`](#insn-007afe18) → `00c7aae8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007afe1c`](#insn-007afe1c) → [`007afe44`](#insn-007afe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afe28`](#insn-007afe28) → [`007afe54`](#insn-007afe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afe40`](#insn-007afe40) → [`007afe48`](#insn-007afe48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afe48`](#insn-007afe48) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afe4c`](#insn-007afe4c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afe64`](#insn-007afe64) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afe68`](#insn-007afe68) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007afdfc`](#insn-007afdfc)

~~~json
{
  "source": "007afdfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afe00`](#insn-007afe00)

~~~json
{
  "source": "007afe00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afe18`](#insn-007afe18)

~~~json
{
  "source": "007afe18",
  "target": "00c7aae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7aae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007afe1c`](#insn-007afe1c)

~~~json
{
  "source": "007afe1c",
  "target": "007afe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afe28`](#insn-007afe28)

~~~json
{
  "source": "007afe28",
  "target": "007afe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afe40`](#insn-007afe40)

~~~json
{
  "source": "007afe40",
  "target": "007afe48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afe48`](#insn-007afe48)

~~~json
{
  "source": "007afe48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afe4c`](#insn-007afe4c)

~~~json
{
  "source": "007afe4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afe64`](#insn-007afe64)

~~~json
{
  "source": "007afe64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afe68`](#insn-007afe68)

~~~json
{
  "source": "007afe68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
