# 00b6addc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b6ad14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ad14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0073.md#compare-98e9c4f2f5e485c6ff2e29b1bb47d532)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6ae20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ae20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0074.md#compare-e5e82ffb659a6d4ce38340a896268a17)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6addc",
  "name": "_ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed2a9fe3c2749cc7e0759da0b730520b864554c075b5221630560ebc436a316a",
  "source_text_sha256": "ed2a9fe3c2749cc7e0759da0b730520b864554c075b5221630560ebc436a316a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6addc",
        "00b6ae7f"
      ]
    ],
    "bytes_sha256": "6179a0dbf7b4dc3b3be6844d8ec537e6bf5e16aa57880124ef74cb415036354b",
    "instruction_count": 41,
    "instruction_bytes": 164,
    "body_bytes": 164,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00be0df0](../00be0/00be0df0.md)

## 呼び出し先

- [00bde130](../00bde/00bde130.md)
- [00bde1b0](../00bde/00bde1b0.md)
- [00bde390](../00bde/00bde390.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 748 bytes

~~~c

void _ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject(long *param_1,long param_2)

{
  long lVar1;
  long *plVar2;
  
  if (*param_1 != 0) {
    lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
    if (lVar1 == 0) {
      _ZN8firebase9LogAssertEPKcz("app != nullptr");
    }
    plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
    (**(code **)(*plVar2 + 0xb0))(plVar2,*param_1);
    *param_1 = 0;
  }
  lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
  if (lVar1 == 0) {
    _ZN8firebase9LogAssertEPKcz("app != nullptr");
  }
  plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
  if (param_2 == 0) {
    lVar1 = 0;
  }
  else {
    lVar1 = (**(code **)(*plVar2 + 0xa8))(plVar2,param_2);
  }
  *param_1 = lVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6addc"></a> `00b6addc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b6ade0"></a> `00b6ade0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ade4"></a> `00b6ade4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6ade8"></a> `00b6ade8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b6adec"></a> `00b6adec` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b6adf0"></a> `00b6adf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b6adf4"></a> `00b6adf4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b6adf8"></a> `00b6adf8` | `c8 01 00 b4` | cbz x8,0x00b6ae30 | `CONDITIONAL_JUMP`
<a id="insn-00b6adfc"></a> `00b6adfc` | `65 cd 01 94` | bl 0x00bde390 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ae00"></a> `00b6ae00` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b6ae04"></a> `00b6ae04` | `80 00 00 b5` | cbnz x0,0x00b6ae14 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae08"></a> `00b6ae08` | `a0 b9 ff f0` | adrp x0,0x2a1000 | `FALL_THROUGH`
<a id="insn-00b6ae0c"></a> `00b6ae0c` | `00 30 39 91` | add x0,x0,#0xe4c | `FALL_THROUGH`
<a id="insn-00b6ae10"></a> `00b6ae10` | `c8 cc 01 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ae14"></a> `00b6ae14` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b6ae18"></a> `00b6ae18` | `e6 cc 01 94` | bl 0x00bde1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ae1c"></a> `00b6ae1c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b6ae20"></a> `00b6ae20` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00b6ae24"></a> `00b6ae24` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00b6ae28"></a> `00b6ae28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b6ae2c"></a> `00b6ae2c` | `7f 02 00 f9` | str xzr,[x19] | `FALL_THROUGH`
<a id="insn-00b6ae30"></a> `00b6ae30` | `58 cd 01 94` | bl 0x00bde390 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ae34"></a> `00b6ae34` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b6ae38"></a> `00b6ae38` | `80 00 00 b5` | cbnz x0,0x00b6ae48 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae3c"></a> `00b6ae3c` | `a0 b9 ff f0` | adrp x0,0x2a1000 | `FALL_THROUGH`
<a id="insn-00b6ae40"></a> `00b6ae40` | `00 30 39 91` | add x0,x0,#0xe4c | `FALL_THROUGH`
<a id="insn-00b6ae44"></a> `00b6ae44` | `bb cc 01 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ae48"></a> `00b6ae48` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b6ae4c"></a> `00b6ae4c` | `d9 cc 01 94` | bl 0x00bde1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ae50"></a> `00b6ae50` | `d4 00 00 b4` | cbz x20,0x00b6ae68 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae54"></a> `00b6ae54` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b6ae58"></a> `00b6ae58` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b6ae5c"></a> `00b6ae5c` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00b6ae60"></a> `00b6ae60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b6ae64"></a> `00b6ae64` | `02 00 00 14` | b 0x00b6ae6c | `UNCONDITIONAL_JUMP`
<a id="insn-00b6ae68"></a> `00b6ae68` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00b6ae6c"></a> `00b6ae6c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00b6ae70"></a> `00b6ae70` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6ae74"></a> `00b6ae74` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ae78"></a> `00b6ae78` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6ae7c"></a> `00b6ae7c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6addc`](#insn-00b6addc) 範囲 `[['00b6addc', '00b6adfb']]`
  - `CONDITIONAL_JUMP` [`00b6adf8`](#insn-00b6adf8) → [`00b6ae30`](#insn-00b6ae30)
  - `FALL_THROUGH` [`00b6adf8`](#insn-00b6adf8) → [`00b6adfc`](#insn-00b6adfc)
- ブロック [`00b6adfc`](#insn-00b6adfc) 範囲 `[['00b6adfc', '00b6ae07']]`
  - `CONDITIONAL_JUMP` [`00b6ae04`](#insn-00b6ae04) → [`00b6ae14`](#insn-00b6ae14)
  - `FALL_THROUGH` [`00b6ae04`](#insn-00b6ae04) → [`00b6ae08`](#insn-00b6ae08)
- ブロック [`00b6ae08`](#insn-00b6ae08) 範囲 `[['00b6ae08', '00b6ae13']]`
  - `FALL_THROUGH` [`00b6ae10`](#insn-00b6ae10) → [`00b6ae14`](#insn-00b6ae14)
- ブロック [`00b6ae14`](#insn-00b6ae14) 範囲 `[['00b6ae14', '00b6ae2f']]`
  - `FALL_THROUGH` [`00b6ae2c`](#insn-00b6ae2c) → [`00b6ae30`](#insn-00b6ae30)
- ブロック [`00b6ae30`](#insn-00b6ae30) 範囲 `[['00b6ae30', '00b6ae3b']]`
  - `CONDITIONAL_JUMP` [`00b6ae38`](#insn-00b6ae38) → [`00b6ae48`](#insn-00b6ae48)
  - `FALL_THROUGH` [`00b6ae38`](#insn-00b6ae38) → [`00b6ae3c`](#insn-00b6ae3c)
- ブロック [`00b6ae3c`](#insn-00b6ae3c) 範囲 `[['00b6ae3c', '00b6ae47']]`
  - `FALL_THROUGH` [`00b6ae44`](#insn-00b6ae44) → [`00b6ae48`](#insn-00b6ae48)
- ブロック [`00b6ae48`](#insn-00b6ae48) 範囲 `[['00b6ae48', '00b6ae53']]`
  - `CONDITIONAL_JUMP` [`00b6ae50`](#insn-00b6ae50) → [`00b6ae68`](#insn-00b6ae68)
  - `FALL_THROUGH` [`00b6ae50`](#insn-00b6ae50) → [`00b6ae54`](#insn-00b6ae54)
- ブロック [`00b6ae54`](#insn-00b6ae54) 範囲 `[['00b6ae54', '00b6ae67']]`
  - `UNCONDITIONAL_JUMP` [`00b6ae64`](#insn-00b6ae64) → [`00b6ae6c`](#insn-00b6ae6c)
- ブロック [`00b6ae68`](#insn-00b6ae68) 範囲 `[['00b6ae68', '00b6ae6b']]`
  - `FALL_THROUGH` [`00b6ae68`](#insn-00b6ae68) → [`00b6ae6c`](#insn-00b6ae6c)
- ブロック [`00b6ae6c`](#insn-00b6ae6c) 範囲 `[['00b6ae6c', '00b6ae7f']]`

## 命令位置別の参照

- [`00b6addc`](#insn-00b6addc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ade0`](#insn-00b6ade0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ade4`](#insn-00b6ade4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6adf8`](#insn-00b6adf8) → [`00b6ae30`](#insn-00b6ae30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6adfc`](#insn-00b6adfc) → [`00bde390`](../00bde/00bde390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde390` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae04`](#insn-00b6ae04) → [`00b6ae14`](#insn-00b6ae14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae0c`](#insn-00b6ae0c) → `002a1e4c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b6ae10`](#insn-00b6ae10) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae18`](#insn-00b6ae18) → [`00bde1b0`](../00bde/00bde1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae30`](#insn-00b6ae30) → [`00bde390`](../00bde/00bde390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde390` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae38`](#insn-00b6ae38) → [`00b6ae48`](#insn-00b6ae48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae40`](#insn-00b6ae40) → `002a1e4c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b6ae44`](#insn-00b6ae44) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae4c`](#insn-00b6ae4c) → [`00bde1b0`](../00bde/00bde1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae50`](#insn-00b6ae50) → [`00b6ae68`](#insn-00b6ae68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae64`](#insn-00b6ae64) → [`00b6ae6c`](#insn-00b6ae6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae70`](#insn-00b6ae70) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae74`](#insn-00b6ae74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6addc`](#insn-00b6addc)

~~~json
{
  "source": "00b6addc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ade0`](#insn-00b6ade0)

~~~json
{
  "source": "00b6ade0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ade4`](#insn-00b6ade4)

~~~json
{
  "source": "00b6ade4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6adf8`](#insn-00b6adf8)

~~~json
{
  "source": "00b6adf8",
  "target": "00b6ae30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6adfc`](#insn-00b6adfc)

~~~json
{
  "source": "00b6adfc",
  "target": "00bde390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ae04`](#insn-00b6ae04)

~~~json
{
  "source": "00b6ae04",
  "target": "00b6ae14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae0c`](#insn-00b6ae0c)

~~~json
{
  "source": "00b6ae0c",
  "target": "002a1e4c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1e4c",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002a1e4c",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b6ae10`](#insn-00b6ae10)

~~~json
{
  "source": "00b6ae10",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ae18`](#insn-00b6ae18)

~~~json
{
  "source": "00b6ae18",
  "target": "00bde1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ae30`](#insn-00b6ae30)

~~~json
{
  "source": "00b6ae30",
  "target": "00bde390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ae38`](#insn-00b6ae38)

~~~json
{
  "source": "00b6ae38",
  "target": "00b6ae48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae40`](#insn-00b6ae40)

~~~json
{
  "source": "00b6ae40",
  "target": "002a1e4c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1e4c",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002a1e4c",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b6ae44`](#insn-00b6ae44)

~~~json
{
  "source": "00b6ae44",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ae4c`](#insn-00b6ae4c)

~~~json
{
  "source": "00b6ae4c",
  "target": "00bde1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ae50`](#insn-00b6ae50)

~~~json
{
  "source": "00b6ae50",
  "target": "00b6ae68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae64`](#insn-00b6ae64)

~~~json
{
  "source": "00b6ae64",
  "target": "00b6ae6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae70`](#insn-00b6ae70)

~~~json
{
  "source": "00b6ae70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae74`](#insn-00b6ae74)

~~~json
{
  "source": "00b6ae74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
