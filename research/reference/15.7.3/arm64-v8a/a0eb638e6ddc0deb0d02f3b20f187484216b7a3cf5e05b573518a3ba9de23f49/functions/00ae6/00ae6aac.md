# 00ae6aac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ae69e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae69e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0059.md#compare-f228623c3ebef0ff10382e8f6ec04916)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ae6af0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6af0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0062.md#compare-9b10319fccdfc70846e1546b770b2197)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae6aac",
  "name": "_ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a098b08c2a572b46fbe6795806a4224206686b6d8bd638973434cfc69c921722",
  "source_text_sha256": "a098b08c2a572b46fbe6795806a4224206686b6d8bd638973434cfc69c921722",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae6aac",
        "00ae6aeb"
      ]
    ],
    "bytes_sha256": "e3fb4887592d5a65a0891e8a127f0769a22e612707ac62cfe0cd36a45b925897",
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
"%PG%dalvik/system/DexClassLoader"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 459 bytes

~~~c

long _ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a0480 == 0) {
    DAT_010a0480 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0480;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae6aac"></a> `00ae6aac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae6ab0"></a> `00ae6ab0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae6ab4"></a> `00ae6ab4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae6ab8"></a> `00ae6ab8` | `d3 2d 00 d0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae6abc"></a> `00ae6abc` | `68 42 42 f9` | ldr x8,[x19, #0x480] | `FALL_THROUGH`
<a id="insn-00ae6ac0"></a> `00ae6ac0` | `e8 00 00 b5` | cbnz x8,0x00ae6adc | `CONDITIONAL_JUMP`
<a id="insn-00ae6ac4"></a> `00ae6ac4` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00ae6ac8"></a> `00ae6ac8` | `03 be ff b0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00ae6acc"></a> `00ae6acc` | `63 00 34 91` | add x3,x3,#0xd00 | `FALL_THROUGH`
<a id="insn-00ae6ad0"></a> `00ae6ad0` | `5c dd 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00ae6ad4"></a> `00ae6ad4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ae6ad8"></a> `00ae6ad8` | `60 42 02 f9` | str x0,[x19, #0x480] | `FALL_THROUGH`
<a id="insn-00ae6adc"></a> `00ae6adc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae6ae0"></a> `00ae6ae0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00ae6ae4"></a> `00ae6ae4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae6ae8"></a> `00ae6ae8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae6aac`](#insn-00ae6aac) 範囲 `[['00ae6aac', '00ae6ac3']]`
  - `CONDITIONAL_JUMP` [`00ae6ac0`](#insn-00ae6ac0) → [`00ae6adc`](#insn-00ae6adc)
  - `FALL_THROUGH` [`00ae6ac0`](#insn-00ae6ac0) → [`00ae6ac4`](#insn-00ae6ac4)
- ブロック [`00ae6ac4`](#insn-00ae6ac4) 範囲 `[['00ae6ac4', '00ae6adb']]`
  - `FALL_THROUGH` [`00ae6ad8`](#insn-00ae6ad8) → [`00ae6adc`](#insn-00ae6adc)
- ブロック [`00ae6adc`](#insn-00ae6adc) 範囲 `[['00ae6adc', '00ae6aeb']]`

## 命令位置別の参照

- [`00ae6aac`](#insn-00ae6aac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6ab0`](#insn-00ae6ab0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6abc`](#insn-00ae6abc) → `010a0480`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae6ac0`](#insn-00ae6ac0) → [`00ae6adc`](#insn-00ae6adc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6acc`](#insn-00ae6acc) → `002a7d00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae6ad0`](#insn-00ae6ad0) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00ae6ad8`](#insn-00ae6ad8) → `010a0480`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae6adc`](#insn-00ae6adc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae6aac`](#insn-00ae6aac)

~~~json
{
  "source": "00ae6aac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6ab0`](#insn-00ae6ab0)

~~~json
{
  "source": "00ae6ab0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6abc`](#insn-00ae6abc)

~~~json
{
  "source": "00ae6abc",
  "target": "010a0480",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0480",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae6ac0`](#insn-00ae6ac0)

~~~json
{
  "source": "00ae6ac0",
  "target": "00ae6adc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6acc`](#insn-00ae6acc)

~~~json
{
  "source": "00ae6acc",
  "target": "002a7d00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7cfc",
  "offset": 4,
  "size": 33,
  "datatype": "string",
  "bytes": "2550472564616c76696b2f73797374656d2f446578436c6173734c6f61646572",
  "capture_start": "002a7cfc",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ae6ad0`](#insn-00ae6ad0)

~~~json
{
  "source": "00ae6ad0",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae6ad8`](#insn-00ae6ad8)

~~~json
{
  "source": "00ae6ad8",
  "target": "010a0480",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0480",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae6adc`](#insn-00ae6adc)

~~~json
{
  "source": "00ae6adc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
