# 00aedcc8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aedc84`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc84.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-3af593b477ef08983e11d2bfedd2ac80)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4da4c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da4c.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-42792b15258806b92bfa4529d7c4f100)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedcc8",
  "name": "_ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8df84ad9b604a33cd73dddf470b88d1c88e64c1d1cc904568f18ed895e51fd0e",
  "source_text_sha256": "8df84ad9b604a33cd73dddf470b88d1c88e64c1d1cc904568f18ed895e51fd0e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedcc8",
        "00aedd0b"
      ]
    ],
    "bytes_sha256": "e190025d7dfea6959929410b36b778aae22bfb11a982ec85f92ecbb5e9c117ee",
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
"android/net/Uri"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 462 bytes

~~~c

long _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a0a60 == 0) {
    DAT_010a0a60 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/net/Uri",param_3);
  }
  return DAT_010a0a60;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedcc8"></a> `00aedcc8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedccc"></a> `00aedccc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedcd0"></a> `00aedcd0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedcd4"></a> `00aedcd4` | `93 2d 00 f0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedcd8"></a> `00aedcd8` | `68 32 45 f9` | ldr x8,[x19, #0xa60] | `FALL_THROUGH`
<a id="insn-00aedcdc"></a> `00aedcdc` | `08 01 00 b5` | cbnz x8,0x00aedcfc | `CONDITIONAL_JUMP`
<a id="insn-00aedce0"></a> `00aedce0` | `43 bd ff d0` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aedce4"></a> `00aedce4` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00aedce8"></a> `00aedce8` | `63 e0 13 91` | add x3,x3,#0x4f8 | `FALL_THROUGH`
<a id="insn-00aedcec"></a> `00aedcec` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aedcf0"></a> `00aedcf0` | `e8 c0 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aedcf4"></a> `00aedcf4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aedcf8"></a> `00aedcf8` | `60 32 05 f9` | str x0,[x19, #0xa60] | `FALL_THROUGH`
<a id="insn-00aedcfc"></a> `00aedcfc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedd00"></a> `00aedd00` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aedd04"></a> `00aedd04` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aedd08"></a> `00aedd08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedcc8`](#insn-00aedcc8) 範囲 `[['00aedcc8', '00aedcdf']]`
  - `CONDITIONAL_JUMP` [`00aedcdc`](#insn-00aedcdc) → [`00aedcfc`](#insn-00aedcfc)
  - `FALL_THROUGH` [`00aedcdc`](#insn-00aedcdc) → [`00aedce0`](#insn-00aedce0)
- ブロック [`00aedce0`](#insn-00aedce0) 範囲 `[['00aedce0', '00aedcfb']]`
  - `FALL_THROUGH` [`00aedcf8`](#insn-00aedcf8) → [`00aedcfc`](#insn-00aedcfc)
- ブロック [`00aedcfc`](#insn-00aedcfc) 範囲 `[['00aedcfc', '00aedd0b']]`

## 命令位置別の参照

- [`00aedcc8`](#insn-00aedcc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedccc`](#insn-00aedccc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedcd8`](#insn-00aedcd8) → `010a0a60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedcdc`](#insn-00aedcdc) → [`00aedcfc`](#insn-00aedcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedce8`](#insn-00aedce8) → `002974f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedcf0`](#insn-00aedcf0) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aedcf8`](#insn-00aedcf8) → `010a0a60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedcfc`](#insn-00aedcfc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedcc8`](#insn-00aedcc8)

~~~json
{
  "source": "00aedcc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedccc`](#insn-00aedccc)

~~~json
{
  "source": "00aedccc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedcd8`](#insn-00aedcd8)

~~~json
{
  "source": "00aedcd8",
  "target": "010a0a60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedcdc`](#insn-00aedcdc)

~~~json
{
  "source": "00aedcdc",
  "target": "00aedcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedce8`](#insn-00aedce8)

~~~json
{
  "source": "00aedce8",
  "target": "002974f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002974f8",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "616e64726f69642f6e65742f55726900",
  "capture_start": "002974f8",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedcf0`](#insn-00aedcf0)

~~~json
{
  "source": "00aedcf0",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedcf8`](#insn-00aedcf8)

~~~json
{
  "source": "00aedcf8",
  "target": "010a0a60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedcfc`](#insn-00aedcfc)

~~~json
{
  "source": "00aedcfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
