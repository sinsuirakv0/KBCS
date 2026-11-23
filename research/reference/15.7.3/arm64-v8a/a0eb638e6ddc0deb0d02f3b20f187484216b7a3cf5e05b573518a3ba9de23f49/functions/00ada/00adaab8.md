# 00adaab8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ada9f0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00ada9f0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-96e8f51bb978767c65b98ccc4e41a174)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00adaafc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaafc.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0007.md#compare-8301ce487f39de0af5b159b3343c9c9c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adaab8",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyConnect",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "12edb31acbfd47cf2d5dda15505b40729a5b7ad3ce51b9b3d9e55d4948ecb157",
  "source_text_sha256": "12edb31acbfd47cf2d5dda15505b40729a5b7ad3ce51b9b3d9e55d4948ecb157",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adaab8",
        "00adab1f"
      ]
    ],
    "bytes_sha256": "1fb917e8b0d39fc762cc176b522e5c6952f0b34f9e21a22e232286386076d36f",
    "instruction_count": 26,
    "instruction_bytes": 104,
    "body_bytes": 104,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 550 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyConnect
               (undefined8 param_1,undefined8 param_2,char param_3)

{
  long lVar1;
  undefined1 local_2c [4];
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  if (DAT_0109ff50 != (long *)0x0) {
    local_2c[0] = param_3 != '\0';
    (**(code **)(*DAT_0109ff50 + 0x30))(DAT_0109ff50,local_2c);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
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
<a id="insn-00adaab8"></a> `00adaab8` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00adaabc"></a> `00adaabc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adaac0"></a> `00adaac0` | `f3 13 00 f9` | str x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adaac4"></a> `00adaac4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00adaac8"></a> `00adaac8` | `53 d0 3b d5` | mrs x19,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adaacc"></a> `00adaacc` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00adaad0"></a> `00adaad0` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adaad4"></a> `00adaad4` | `28 2e 00 b0` | adrp x8,0x109f000 | `FALL_THROUGH`
<a id="insn-00adaad8"></a> `00adaad8` | `00 a9 47 f9` | ldr x0,[x8, #0xf50] | `FALL_THROUGH`
<a id="insn-00adaadc"></a> `00adaadc` | `00 01 00 b4` | cbz x0,0x00adaafc | `CONDITIONAL_JUMP`
<a id="insn-00adaae0"></a> `00adaae0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adaae4"></a> `00adaae4` | `5f 1c 00 72` | tst w2,#0xff | `FALL_THROUGH`
<a id="insn-00adaae8"></a> `00adaae8` | `e1 13 00 91` | add x1,sp,#0x4 | `FALL_THROUGH`
<a id="insn-00adaaec"></a> `00adaaec` | `e9 07 9f 1a` | cset w9,ne | `FALL_THROUGH`
<a id="insn-00adaaf0"></a> `00adaaf0` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00adaaf4"></a> `00adaaf4` | `e9 13 00 39` | strb w9,[sp, #0x4] | `FALL_THROUGH`
<a id="insn-00adaaf8"></a> `00adaaf8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adaafc"></a> `00adaafc` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00adab00"></a> `00adab00` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adab04"></a> `00adab04` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adab08"></a> `00adab08` | `a1 00 00 54` | b.ne 0x00adab1c | `CONDITIONAL_JUMP`
<a id="insn-00adab0c"></a> `00adab0c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adab10"></a> `00adab10` | `f3 13 40 f9` | ldr x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adab14"></a> `00adab14` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00adab18"></a> `00adab18` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adab1c"></a> `00adab1c` | `49 01 04 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adaab8`](#insn-00adaab8) 範囲 `[['00adaab8', '00adaadf']]`
  - `CONDITIONAL_JUMP` [`00adaadc`](#insn-00adaadc) → [`00adaafc`](#insn-00adaafc)
  - `FALL_THROUGH` [`00adaadc`](#insn-00adaadc) → [`00adaae0`](#insn-00adaae0)
- ブロック [`00adaae0`](#insn-00adaae0) 範囲 `[['00adaae0', '00adaafb']]`
  - `FALL_THROUGH` [`00adaaf8`](#insn-00adaaf8) → [`00adaafc`](#insn-00adaafc)
- ブロック [`00adaafc`](#insn-00adaafc) 範囲 `[['00adaafc', '00adab0b']]`
  - `CONDITIONAL_JUMP` [`00adab08`](#insn-00adab08) → [`00adab1c`](#insn-00adab1c)
  - `FALL_THROUGH` [`00adab08`](#insn-00adab08) → [`00adab0c`](#insn-00adab0c)
- ブロック [`00adab0c`](#insn-00adab0c) 範囲 `[['00adab0c', '00adab1b']]`
- ブロック [`00adab1c`](#insn-00adab1c) 範囲 `[['00adab1c', '00adab1f']]`

## 命令位置別の参照

- [`00adaabc`](#insn-00adaabc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaac0`](#insn-00adaac0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaad0`](#insn-00adaad0) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaad8`](#insn-00adaad8) → `0109ff50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adaadc`](#insn-00adaadc) → [`00adaafc`](#insn-00adaafc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaaf4`](#insn-00adaaf4) → `Stack[-0x2c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab00`](#insn-00adab00) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab08`](#insn-00adab08) → [`00adab1c`](#insn-00adab1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab0c`](#insn-00adab0c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab10`](#insn-00adab10) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab1c`](#insn-00adab1c) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adaabc`](#insn-00adaabc)

~~~json
{
  "source": "00adaabc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaac0`](#insn-00adaac0)

~~~json
{
  "source": "00adaac0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaad0`](#insn-00adaad0)

~~~json
{
  "source": "00adaad0",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaad8`](#insn-00adaad8)

~~~json
{
  "source": "00adaad8",
  "target": "0109ff50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adaadc`](#insn-00adaadc)

~~~json
{
  "source": "00adaadc",
  "target": "00adaafc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaaf4`](#insn-00adaaf4)

~~~json
{
  "source": "00adaaf4",
  "target": "Stack[-0x2c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab00`](#insn-00adab00)

~~~json
{
  "source": "00adab00",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab08`](#insn-00adab08)

~~~json
{
  "source": "00adab08",
  "target": "00adab1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab0c`](#insn-00adab0c)

~~~json
{
  "source": "00adab0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab10`](#insn-00adab10)

~~~json
{
  "source": "00adab10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab1c`](#insn-00adab1c)

~~~json
{
  "source": "00adab1c",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
