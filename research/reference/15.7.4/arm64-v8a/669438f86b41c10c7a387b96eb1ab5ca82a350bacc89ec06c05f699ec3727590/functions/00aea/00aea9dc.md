# 00aea9dc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aea998`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea998.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-b7d577a9b44a4bb6242b30dca28ad3f0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4a760`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a760.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-f9ab7d46cbae34ee8b165af51e003ba3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aea9dc",
  "name": "_ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7b19bf8cb188980fa85ff5f048db4ced5b24a8411bc19abf6b18c9689fb87eba",
  "source_text_sha256": "7b19bf8cb188980fa85ff5f048db4ced5b24a8411bc19abf6b18c9689fb87eba",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aea9dc",
        "00aeaa1f"
      ]
    ],
    "bytes_sha256": "ed5504a221c68d49bc8c7aa0e462cc052f4229e8d37bc4c10d0d5d5f118f66a6",
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
"java/lang/Float"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 423 bytes

~~~c

long _ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0828 == 0) {
    DAT_010a0828 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Float",0);
  }
  return DAT_010a0828;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aea9dc"></a> `00aea9dc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aea9e0"></a> `00aea9e0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea9e4"></a> `00aea9e4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aea9e8"></a> `00aea9e8` | `b3 2d 00 d0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aea9ec"></a> `00aea9ec` | `68 16 44 f9` | ldr x8,[x19, #0x828] | `FALL_THROUGH`
<a id="insn-00aea9f0"></a> `00aea9f0` | `08 01 00 b5` | cbnz x8,0x00aeaa10 | `CONDITIONAL_JUMP`
<a id="insn-00aea9f4"></a> `00aea9f4` | `63 bd ff f0` | adrp x3,0x299000 | `FALL_THROUGH`
<a id="insn-00aea9f8"></a> `00aea9f8` | `63 50 19 91` | add x3,x3,#0x654 | `FALL_THROUGH`
<a id="insn-00aea9fc"></a> `00aea9fc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeaa00"></a> `00aeaa00` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aeaa04"></a> `00aeaa04` | `a3 cd 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aeaa08"></a> `00aeaa08` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aeaa0c"></a> `00aeaa0c` | `60 16 04 f9` | str x0,[x19, #0x828] | `FALL_THROUGH`
<a id="insn-00aeaa10"></a> `00aeaa10` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaa14"></a> `00aeaa14` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aeaa18"></a> `00aeaa18` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeaa1c"></a> `00aeaa1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aea9dc`](#insn-00aea9dc) 範囲 `[['00aea9dc', '00aea9f3']]`
  - `CONDITIONAL_JUMP` [`00aea9f0`](#insn-00aea9f0) → [`00aeaa10`](#insn-00aeaa10)
  - `FALL_THROUGH` [`00aea9f0`](#insn-00aea9f0) → [`00aea9f4`](#insn-00aea9f4)
- ブロック [`00aea9f4`](#insn-00aea9f4) 範囲 `[['00aea9f4', '00aeaa0f']]`
  - `FALL_THROUGH` [`00aeaa0c`](#insn-00aeaa0c) → [`00aeaa10`](#insn-00aeaa10)
- ブロック [`00aeaa10`](#insn-00aeaa10) 範囲 `[['00aeaa10', '00aeaa1f']]`

## 命令位置別の参照

- [`00aea9dc`](#insn-00aea9dc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea9e0`](#insn-00aea9e0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea9ec`](#insn-00aea9ec) → `010a0828`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aea9f0`](#insn-00aea9f0) → [`00aeaa10`](#insn-00aeaa10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea9f8`](#insn-00aea9f8) → `00299654`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeaa04`](#insn-00aeaa04) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aeaa0c`](#insn-00aeaa0c) → `010a0828`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaa10`](#insn-00aeaa10) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aea9dc`](#insn-00aea9dc)

~~~json
{
  "source": "00aea9dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea9e0`](#insn-00aea9e0)

~~~json
{
  "source": "00aea9e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea9ec`](#insn-00aea9ec)

~~~json
{
  "source": "00aea9ec",
  "target": "010a0828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0828",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea9f0`](#insn-00aea9f0)

~~~json
{
  "source": "00aea9f0",
  "target": "00aeaa10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea9f8`](#insn-00aea9f8)

~~~json
{
  "source": "00aea9f8",
  "target": "00299654",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00299654",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f466c6f617400",
  "capture_start": "00299654",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeaa04`](#insn-00aeaa04)

~~~json
{
  "source": "00aeaa04",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaa0c`](#insn-00aeaa0c)

~~~json
{
  "source": "00aeaa0c",
  "target": "010a0828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0828",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaa10`](#insn-00aeaa10)

~~~json
{
  "source": "00aeaa10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
