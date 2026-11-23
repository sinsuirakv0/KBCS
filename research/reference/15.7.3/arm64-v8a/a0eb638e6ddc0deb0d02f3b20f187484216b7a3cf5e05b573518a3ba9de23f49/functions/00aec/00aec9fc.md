# 00aec9fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aec934`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec934.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-f08218670053417b1c366f22c03d8b23)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeca40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-d8ba3efc9e5eb230bc875c940b916140)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aec9fc",
  "name": "_ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "848b6e2fdbd6f53c120b2b66cd24c1db1f4e3173b85551d424a75fcc2b1296ec",
  "source_text_sha256": "848b6e2fdbd6f53c120b2b66cd24c1db1f4e3173b85551d424a75fcc2b1296ec",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aec9fc",
        "00aeca3b"
      ]
    ],
    "bytes_sha256": "c90a6f82dd9c9812f228438c6594a71ab19356153cf1262bb34ab95200839a34",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
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
"android/os/ParcelFileDescriptor"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 442 bytes

~~~c

long _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a0968 == 0) {
    DAT_010a0968 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0968;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aec9fc"></a> `00aec9fc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeca00"></a> `00aeca00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeca04"></a> `00aeca04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeca08"></a> `00aeca08` | `b3 2d 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeca0c"></a> `00aeca0c` | `68 b6 44 f9` | ldr x8,[x19, #0x968] | `FALL_THROUGH`
<a id="insn-00aeca10"></a> `00aeca10` | `e8 00 00 b5` | cbnz x8,0x00aeca2c | `CONDITIONAL_JUMP`
<a id="insn-00aeca14"></a> `00aeca14` | `43 bd ff 90` | adrp x3,0x294000 | `FALL_THROUGH`
<a id="insn-00aeca18"></a> `00aeca18` | `63 80 09 91` | add x3,x3,#0x260 | `FALL_THROUGH`
<a id="insn-00aeca1c"></a> `00aeca1c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aeca20"></a> `00aeca20` | `88 c5 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aeca24"></a> `00aeca24` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aeca28"></a> `00aeca28` | `60 b6 04 f9` | str x0,[x19, #0x968] | `FALL_THROUGH`
<a id="insn-00aeca2c"></a> `00aeca2c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeca30"></a> `00aeca30` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aeca34"></a> `00aeca34` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeca38"></a> `00aeca38` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aec9fc`](#insn-00aec9fc) 範囲 `[['00aec9fc', '00aeca13']]`
  - `CONDITIONAL_JUMP` [`00aeca10`](#insn-00aeca10) → [`00aeca2c`](#insn-00aeca2c)
  - `FALL_THROUGH` [`00aeca10`](#insn-00aeca10) → [`00aeca14`](#insn-00aeca14)
- ブロック [`00aeca14`](#insn-00aeca14) 範囲 `[['00aeca14', '00aeca2b']]`
  - `FALL_THROUGH` [`00aeca28`](#insn-00aeca28) → [`00aeca2c`](#insn-00aeca2c)
- ブロック [`00aeca2c`](#insn-00aeca2c) 範囲 `[['00aeca2c', '00aeca3b']]`

## 命令位置別の参照

- [`00aec9fc`](#insn-00aec9fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeca00`](#insn-00aeca00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeca0c`](#insn-00aeca0c) → `010a0968`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeca10`](#insn-00aeca10) → [`00aeca2c`](#insn-00aeca2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeca18`](#insn-00aeca18) → `00294260`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeca20`](#insn-00aeca20) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aeca28`](#insn-00aeca28) → `010a0968`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeca2c`](#insn-00aeca2c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aec9fc`](#insn-00aec9fc)

~~~json
{
  "source": "00aec9fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeca00`](#insn-00aeca00)

~~~json
{
  "source": "00aeca00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeca0c`](#insn-00aeca0c)

~~~json
{
  "source": "00aeca0c",
  "target": "010a0968",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0968",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeca10`](#insn-00aeca10)

~~~json
{
  "source": "00aeca10",
  "target": "00aeca2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeca18`](#insn-00aeca18)

~~~json
{
  "source": "00aeca18",
  "target": "00294260",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00294260",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "616e64726f69642f6f732f50617263656c46696c6544657363726970746f7200",
  "capture_start": "00294260",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeca20`](#insn-00aeca20)

~~~json
{
  "source": "00aeca20",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeca28`](#insn-00aeca28)

~~~json
{
  "source": "00aeca28",
  "target": "010a0968",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0968",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeca2c`](#insn-00aeca2c)

~~~json
{
  "source": "00aeca2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
