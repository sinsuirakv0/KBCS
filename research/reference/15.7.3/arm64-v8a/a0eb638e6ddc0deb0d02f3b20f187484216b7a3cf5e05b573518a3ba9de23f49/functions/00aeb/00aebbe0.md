# 00aebbe0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aebb18`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebb18.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-75e2b11c6602cacc2216146f217b7927)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aebc24`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc24.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-05def5ba071b17bf693f56e08a36851f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebbe0",
  "name": "_ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d0e443c830c1ab6d432e691f1a2acb193735a2a292744543afcb1e8a0002c120",
  "source_text_sha256": "d0e443c830c1ab6d432e691f1a2acb193735a2a292744543afcb1e8a0002c120",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebbe0",
        "00aebc23"
      ]
    ],
    "bytes_sha256": "303bca3242b54335c777af27826245d57d1701a85e8abaeaea25720e2f9c1978",
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

- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Iterator"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 422 bytes

~~~c

long _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a08b8 == 0) {
    DAT_010a08b8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Iterator",0);
  }
  return DAT_010a08b8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebbe0"></a> `00aebbe0` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebbe4"></a> `00aebbe4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebbe8"></a> `00aebbe8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebbec"></a> `00aebbec` | `b3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebbf0"></a> `00aebbf0` | `68 5e 44 f9` | ldr x8,[x19, #0x8b8] | `FALL_THROUGH`
<a id="insn-00aebbf4"></a> `00aebbf4` | `08 01 00 b5` | cbnz x8,0x00aebc14 | `CONDITIONAL_JUMP`
<a id="insn-00aebbf8"></a> `00aebbf8` | `63 bd ff 90` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aebbfc"></a> `00aebbfc` | `63 9c 15 91` | add x3,x3,#0x567 | `FALL_THROUGH`
<a id="insn-00aebc00"></a> `00aebc00` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aebc04"></a> `00aebc04` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aebc08"></a> `00aebc08` | `0e c9 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aebc0c"></a> `00aebc0c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aebc10"></a> `00aebc10` | `60 5e 04 f9` | str x0,[x19, #0x8b8] | `FALL_THROUGH`
<a id="insn-00aebc14"></a> `00aebc14` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebc18"></a> `00aebc18` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aebc1c"></a> `00aebc1c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebc20"></a> `00aebc20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebbe0`](#insn-00aebbe0) 範囲 `[['00aebbe0', '00aebbf7']]`
  - `CONDITIONAL_JUMP` [`00aebbf4`](#insn-00aebbf4) → [`00aebc14`](#insn-00aebc14)
  - `FALL_THROUGH` [`00aebbf4`](#insn-00aebbf4) → [`00aebbf8`](#insn-00aebbf8)
- ブロック [`00aebbf8`](#insn-00aebbf8) 範囲 `[['00aebbf8', '00aebc13']]`
  - `FALL_THROUGH` [`00aebc10`](#insn-00aebc10) → [`00aebc14`](#insn-00aebc14)
- ブロック [`00aebc14`](#insn-00aebc14) 範囲 `[['00aebc14', '00aebc23']]`

## 命令位置別の参照

- [`00aebbe0`](#insn-00aebbe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebbe4`](#insn-00aebbe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebbf0`](#insn-00aebbf0) → `010a08b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebbf4`](#insn-00aebbf4) → [`00aebc14`](#insn-00aebc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebbfc`](#insn-00aebbfc) → `00297567`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebc08`](#insn-00aebc08) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aebc10`](#insn-00aebc10) → `010a08b8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebc14`](#insn-00aebc14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebbe0`](#insn-00aebbe0)

~~~json
{
  "source": "00aebbe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebbe4`](#insn-00aebbe4)

~~~json
{
  "source": "00aebbe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebbf0`](#insn-00aebbf0)

~~~json
{
  "source": "00aebbf0",
  "target": "010a08b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebbf4`](#insn-00aebbf4)

~~~json
{
  "source": "00aebbf4",
  "target": "00aebc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebbfc`](#insn-00aebbfc)

~~~json
{
  "source": "00aebbfc",
  "target": "00297567",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00297567",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4974657261746f7200",
  "capture_start": "00297567",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebc08`](#insn-00aebc08)

~~~json
{
  "source": "00aebc08",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebc10`](#insn-00aebc10)

~~~json
{
  "source": "00aebc10",
  "target": "010a08b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebc14`](#insn-00aebc14)

~~~json
{
  "source": "00aebc14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
