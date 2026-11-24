# 00b6faac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b6fa68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fa68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0010.md#compare-8bcc275561cd1e15a70d5f7f6b52f452)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdefac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bdefac.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0071.md#compare-7adb0be130d35614ea771180ecd9230c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6faac",
  "name": "_ZNK8firebase4auth22AndroidWrappedUserInfo3uidEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "492d5808946dc6a4b860158c6b3aa0cdbe9038fe14c381bf325af066702a4bdd",
  "source_text_sha256": "492d5808946dc6a4b860158c6b3aa0cdbe9038fe14c381bf325af066702a4bdd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6faac",
        "00b6fb2f"
      ]
    ],
    "bytes_sha256": "ef47a1f3db3324c478dea80b89530df60e82f5a3b22c7b021accb3b9eee1955c",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bde0e0](../00bde/00bde0e0.md)
- [00bde200](../00bde/00bde200.md)
- [00bde510](../00bde/00bde510.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 642 bytes

~~~c

void _ZNK8firebase4auth22AndroidWrappedUserInfo3uidEv(undefined8 *param_1,long param_2)

{
  long lVar1;
  undefined8 uVar2;
  long lVar3;
  ulong uVar4;
  
  lVar1 = *(long *)(param_2 + 0xa0);
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
  lVar3 = 0;
  if (lVar1 != 0) {
    lVar3 = FUN_0047495c(uVar2,lVar1,DAT_010a1ab8);
  }
  uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar2);
  if ((lVar3 != 0) && ((uVar4 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar2,lVar3);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6faac"></a> `00b6faac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b6fab0"></a> `00b6fab0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fab4"></a> `00b6fab4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6fab8"></a> `00b6fab8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b6fabc"></a> `00b6fabc` | `09 d4 49 a9` | ldp x9,x21,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00b6fac0"></a> `00b6fac0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b6fac4"></a> `00b6fac4` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00b6fac8"></a> `00b6fac8` | `ce b9 01 94` | bl 0x00bde200 | `UNCONDITIONAL_CALL`
<a id="insn-00b6facc"></a> `00b6facc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b6fad0"></a> `00b6fad0` | `f5 00 00 b4` | cbz x21,0x00b6faec | `CONDITIONAL_JUMP`
<a id="insn-00b6fad4"></a> `00b6fad4` | `88 29 00 d0` | adrp x8,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6fad8"></a> `00b6fad8` | `02 5d 45 f9` | ldr x2,[x8, #0xab8] | `FALL_THROUGH`
<a id="insn-00b6fadc"></a> `00b6fadc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6fae0"></a> `00b6fae0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b6fae4"></a> `00b6fae4` | `9e 13 e4 97` | bl 0x0047495c | `UNCONDITIONAL_CALL`
<a id="insn-00b6fae8"></a> `00b6fae8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b6faec"></a> `00b6faec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6faf0"></a> `00b6faf0` | `7c b9 01 94` | bl 0x00bde0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6faf4"></a> `00b6faf4` | `35 01 00 b4` | cbz x21,0x00b6fb18 | `CONDITIONAL_JUMP`
<a id="insn-00b6faf8"></a> `00b6faf8` | `00 01 00 37` | tbnz w0,#0x0,0x00b6fb18 | `CONDITIONAL_JUMP`
<a id="insn-00b6fafc"></a> `00b6fafc` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b6fb00"></a> `00b6fb00` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6fb04"></a> `00b6fb04` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6fb08"></a> `00b6fb08` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fb0c"></a> `00b6fb0c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b6fb10"></a> `00b6fb10` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6fb14"></a> `00b6fb14` | `7f ba 01 14` | b 0x00bde510 | `CALL_TERMINATOR`
<a id="insn-00b6fb18"></a> `00b6fb18` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00b6fb1c"></a> `00b6fb1c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fb20"></a> `00b6fb20` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6fb24"></a> `00b6fb24` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fb28"></a> `00b6fb28` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6fb2c"></a> `00b6fb2c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6faac`](#insn-00b6faac) 範囲 `[['00b6faac', '00b6fad3']]`
  - `CONDITIONAL_JUMP` [`00b6fad0`](#insn-00b6fad0) → [`00b6faec`](#insn-00b6faec)
  - `FALL_THROUGH` [`00b6fad0`](#insn-00b6fad0) → [`00b6fad4`](#insn-00b6fad4)
- ブロック [`00b6fad4`](#insn-00b6fad4) 範囲 `[['00b6fad4', '00b6faeb']]`
  - `FALL_THROUGH` [`00b6fae8`](#insn-00b6fae8) → [`00b6faec`](#insn-00b6faec)
- ブロック [`00b6faec`](#insn-00b6faec) 範囲 `[['00b6faec', '00b6faf7']]`
  - `CONDITIONAL_JUMP` [`00b6faf4`](#insn-00b6faf4) → [`00b6fb18`](#insn-00b6fb18)
  - `FALL_THROUGH` [`00b6faf4`](#insn-00b6faf4) → [`00b6faf8`](#insn-00b6faf8)
- ブロック [`00b6faf8`](#insn-00b6faf8) 範囲 `[['00b6faf8', '00b6fafb']]`
  - `CONDITIONAL_JUMP` [`00b6faf8`](#insn-00b6faf8) → [`00b6fb18`](#insn-00b6fb18)
  - `FALL_THROUGH` [`00b6faf8`](#insn-00b6faf8) → [`00b6fafc`](#insn-00b6fafc)
- ブロック [`00b6fafc`](#insn-00b6fafc) 範囲 `[['00b6fafc', '00b6fb17']]`
- ブロック [`00b6fb18`](#insn-00b6fb18) 範囲 `[['00b6fb18', '00b6fb2f']]`

## 命令位置別の参照

- [`00b6faac`](#insn-00b6faac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fab0`](#insn-00b6fab0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fab4`](#insn-00b6fab4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fac8`](#insn-00b6fac8) → [`00bde200`](../00bde/00bde200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde200` · 推定シンボル `None` · 推定型 `None`
- [`00b6fad0`](#insn-00b6fad0) → [`00b6faec`](#insn-00b6faec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fad8`](#insn-00b6fad8) → `010a1ab8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6fae4`](#insn-00b6fae4) → [`0047495c`](../00474/0047495c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047495c` · 推定シンボル `None` · 推定型 `None`
- [`00b6faf0`](#insn-00b6faf0) → [`00bde0e0`](../00bde/00bde0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0e0` · 推定シンボル `None` · 推定型 `None`
- [`00b6faf4`](#insn-00b6faf4) → [`00b6fb18`](#insn-00b6fb18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6faf8`](#insn-00b6faf8) → [`00b6fb18`](#insn-00b6fb18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb04`](#insn-00b6fb04) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb08`](#insn-00b6fb08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb14`](#insn-00b6fb14) → [`00bde510`](../00bde/00bde510.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde510` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb20`](#insn-00b6fb20) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb24`](#insn-00b6fb24) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6faac`](#insn-00b6faac)

~~~json
{
  "source": "00b6faac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fab0`](#insn-00b6fab0)

~~~json
{
  "source": "00b6fab0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fab4`](#insn-00b6fab4)

~~~json
{
  "source": "00b6fab4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fac8`](#insn-00b6fac8)

~~~json
{
  "source": "00b6fac8",
  "target": "00bde200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fad0`](#insn-00b6fad0)

~~~json
{
  "source": "00b6fad0",
  "target": "00b6faec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fad8`](#insn-00b6fad8)

~~~json
{
  "source": "00b6fad8",
  "target": "010a1ab8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1ab8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6fae4`](#insn-00b6fae4)

~~~json
{
  "source": "00b6fae4",
  "target": "0047495c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6faf0`](#insn-00b6faf0)

~~~json
{
  "source": "00b6faf0",
  "target": "00bde0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6faf4`](#insn-00b6faf4)

~~~json
{
  "source": "00b6faf4",
  "target": "00b6fb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6faf8`](#insn-00b6faf8)

~~~json
{
  "source": "00b6faf8",
  "target": "00b6fb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb04`](#insn-00b6fb04)

~~~json
{
  "source": "00b6fb04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb08`](#insn-00b6fb08)

~~~json
{
  "source": "00b6fb08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb14`](#insn-00b6fb14)

~~~json
{
  "source": "00b6fb14",
  "target": "00bde510",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fb20`](#insn-00b6fb20)

~~~json
{
  "source": "00b6fb20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb24`](#insn-00b6fb24)

~~~json
{
  "source": "00b6fb24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
