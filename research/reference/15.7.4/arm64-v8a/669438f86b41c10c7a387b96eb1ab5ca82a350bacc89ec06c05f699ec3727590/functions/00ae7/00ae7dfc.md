# 00ae7dfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae7db8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7db8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0062.md#compare-644580e6fb6b2316cfc8f0e8b002ebf1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b47b80`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47b80.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0057.md#compare-3032ea55a395446a8256eae0b89fd4f4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae7dfc",
  "name": "_ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2ddc951527f741d8fb9106b35385957168017962bdfd8aae118d6ae29dfaaac7",
  "source_text_sha256": "2ddc951527f741d8fb9106b35385957168017962bdfd8aae118d6ae29dfaaac7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae7dfc",
        "00ae7e3f"
      ]
    ],
    "bytes_sha256": "9bd06ac980bce6e6a2ab5c928c740cac40f879b3c54ca49d8fe419c888e396f9",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Boolean"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 621 bytes

~~~c

long _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00ae7e04 to 00be7e0b has its CatchHandler @ 00ae8c68 */
  if (DAT_010a05c0 == 0) {
    DAT_010a05c0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Boolean",0);
  }
                    /* try { // try from 00ae7e3c to 00be7e47 has its CatchHandler @ 00ae8c64 */
  return DAT_010a05c0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae7dfc"></a> `00ae7dfc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae7e00"></a> `00ae7e00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae7e04"></a> `00ae7e04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae7e08"></a> `00ae7e08` | `d3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae7e0c"></a> `00ae7e0c` | `68 e2 42 f9` | ldr x8,[x19, #0x5c0] | `FALL_THROUGH`
<a id="insn-00ae7e10"></a> `00ae7e10` | `08 01 00 b5` | cbnz x8,0x00ae7e30 | `CONDITIONAL_JUMP`
<a id="insn-00ae7e14"></a> `00ae7e14` | `83 bd ff b0` | adrp x3,0x298000 | `FALL_THROUGH`
<a id="insn-00ae7e18"></a> `00ae7e18` | `63 70 17 91` | add x3,x3,#0x5dc | `FALL_THROUGH`
<a id="insn-00ae7e1c"></a> `00ae7e1c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ae7e20"></a> `00ae7e20` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00ae7e24"></a> `00ae7e24` | `9b d8 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00ae7e28"></a> `00ae7e28` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ae7e2c"></a> `00ae7e2c` | `60 e2 02 f9` | str x0,[x19, #0x5c0] | `FALL_THROUGH`
<a id="insn-00ae7e30"></a> `00ae7e30` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae7e34"></a> `00ae7e34` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00ae7e38"></a> `00ae7e38` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae7e3c"></a> `00ae7e3c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae7dfc`](#insn-00ae7dfc) 範囲 `[['00ae7dfc', '00ae7e03']]`
  - `FALL_THROUGH` [`00ae7e00`](#insn-00ae7e00) → [`00ae7e04`](#insn-00ae7e04)
- ブロック [`00ae7e04`](#insn-00ae7e04) 範囲 `[['00ae7e04', '00ae7e13']]`
  - `CONDITIONAL_JUMP` [`00ae7e10`](#insn-00ae7e10) → [`00ae7e30`](#insn-00ae7e30)
  - `FALL_THROUGH` [`00ae7e10`](#insn-00ae7e10) → [`00ae7e14`](#insn-00ae7e14)
- ブロック [`00ae7e14`](#insn-00ae7e14) 範囲 `[['00ae7e14', '00ae7e2f']]`
  - `FALL_THROUGH` [`00ae7e2c`](#insn-00ae7e2c) → [`00ae7e30`](#insn-00ae7e30)
- ブロック [`00ae7e30`](#insn-00ae7e30) 範囲 `[['00ae7e30', '00ae7e3b']]`
  - `FALL_THROUGH` [`00ae7e38`](#insn-00ae7e38) → [`00ae7e3c`](#insn-00ae7e3c)
- ブロック [`00ae7e3c`](#insn-00ae7e3c) 範囲 `[['00ae7e3c', '00ae7e3f']]`

## 命令位置別の参照

- [`00ae7dfc`](#insn-00ae7dfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7e00`](#insn-00ae7e00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7e0c`](#insn-00ae7e0c) → `010a05c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae7e10`](#insn-00ae7e10) → [`00ae7e30`](#insn-00ae7e30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7e18`](#insn-00ae7e18) → `002985dc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae7e24`](#insn-00ae7e24) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00ae7e2c`](#insn-00ae7e2c) → `010a05c0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae7e30`](#insn-00ae7e30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae7dfc`](#insn-00ae7dfc)

~~~json
{
  "source": "00ae7dfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7e00`](#insn-00ae7e00)

~~~json
{
  "source": "00ae7e00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7e0c`](#insn-00ae7e0c)

~~~json
{
  "source": "00ae7e0c",
  "target": "010a05c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a05c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7e10`](#insn-00ae7e10)

~~~json
{
  "source": "00ae7e10",
  "target": "00ae7e30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7e18`](#insn-00ae7e18)

~~~json
{
  "source": "00ae7e18",
  "target": "002985dc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002985dc",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f426f6f6c65616e00",
  "capture_start": "002985dc",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae7e24`](#insn-00ae7e24)

~~~json
{
  "source": "00ae7e24",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae7e2c`](#insn-00ae7e2c)

~~~json
{
  "source": "00ae7e2c",
  "target": "010a05c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a05c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7e30`](#insn-00ae7e30)

~~~json
{
  "source": "00ae7e30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
