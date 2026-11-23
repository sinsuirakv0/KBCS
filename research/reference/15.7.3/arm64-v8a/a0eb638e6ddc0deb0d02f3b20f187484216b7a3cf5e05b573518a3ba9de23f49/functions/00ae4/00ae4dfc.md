# 00ae4dfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ae4d34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4d34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0058.md#compare-6445b2e79ed9ac37e13de608b108beb1)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ae4e40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0061.md#compare-6dba8ad65b0cacad512f0f6ac87ea54b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae4dfc",
  "name": "_ZN8firebase4util12class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f32f82c073109e2090e54a679c3c93a837c0b6b8a88a2d77d87586b7b6eb406d",
  "source_text_sha256": "f32f82c073109e2090e54a679c3c93a837c0b6b8a88a2d77d87586b7b6eb406d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae4dfc",
        "00ae4e6b"
      ]
    ],
    "bytes_sha256": "6c8893f077934d1cec1a6e035f26b0ef334c345b5a0f8a19ebc61dfbf17fcbc3",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde020](../00bde/00bde020.md)
- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/ClassLoader"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 605 bytes

~~~c

void _ZN8firebase4util12class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0328 == 0) {
    DAT_010a0328 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/ClassLoader",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a0328,&DAT_002f5a58,1,&DAT_010a0348,"java/lang/ClassLoader");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae4dfc"></a> `00ae4dfc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae4e00"></a> `00ae4e00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae4e04"></a> `00ae4e04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae4e08"></a> `00ae4e08` | `f4 2d 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae4e0c"></a> `00ae4e0c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00ae4e10"></a> `00ae4e10` | `81 96 41 f9` | ldr x1,[x20, #0x328] | `FALL_THROUGH`
<a id="insn-00ae4e14"></a> `00ae4e14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ae4e18"></a> `00ae4e18` | `41 01 00 b5` | cbnz x1,0x00ae4e40 | `CONDITIONAL_JUMP`
<a id="insn-00ae4e1c"></a> `00ae4e1c` | `03 be ff f0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00ae4e20"></a> `00ae4e20` | `63 40 33 91` | add x3,x3,#0xcd0 | `FALL_THROUGH`
<a id="insn-00ae4e24"></a> `00ae4e24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae4e28"></a> `00ae4e28` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00ae4e2c"></a> `00ae4e2c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ae4e30"></a> `00ae4e30` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00ae4e34"></a> `00ae4e34` | `83 e4 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00ae4e38"></a> `00ae4e38` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ae4e3c"></a> `00ae4e3c` | `80 96 01 f9` | str x0,[x20, #0x328] | `FALL_THROUGH`
<a id="insn-00ae4e40"></a> `00ae4e40` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae4e44"></a> `00ae4e44` | `82 c0 ff b0` | adrp x2,0x2f5000 | `FALL_THROUGH`
<a id="insn-00ae4e48"></a> `00ae4e48` | `e4 2d 00 90` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae4e4c"></a> `00ae4e4c` | `05 be ff f0` | adrp x5,0x2a7000 | `FALL_THROUGH`
<a id="insn-00ae4e50"></a> `00ae4e50` | `42 60 29 91` | add x2,x2,#0xa58 | `FALL_THROUGH`
<a id="insn-00ae4e54"></a> `00ae4e54` | `84 20 0d 91` | add x4,x4,#0x348 | `FALL_THROUGH`
<a id="insn-00ae4e58"></a> `00ae4e58` | `a5 40 33 91` | add x5,x5,#0xcd0 | `FALL_THROUGH`
<a id="insn-00ae4e5c"></a> `00ae4e5c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00ae4e60"></a> `00ae4e60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae4e64"></a> `00ae4e64` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae4e68"></a> `00ae4e68` | `6e e4 03 14` | b 0x00bde020 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae4dfc`](#insn-00ae4dfc) 範囲 `[['00ae4dfc', '00ae4e1b']]`
  - `CONDITIONAL_JUMP` [`00ae4e18`](#insn-00ae4e18) → [`00ae4e40`](#insn-00ae4e40)
  - `FALL_THROUGH` [`00ae4e18`](#insn-00ae4e18) → [`00ae4e1c`](#insn-00ae4e1c)
- ブロック [`00ae4e1c`](#insn-00ae4e1c) 範囲 `[['00ae4e1c', '00ae4e3f']]`
  - `FALL_THROUGH` [`00ae4e3c`](#insn-00ae4e3c) → [`00ae4e40`](#insn-00ae4e40)
- ブロック [`00ae4e40`](#insn-00ae4e40) 範囲 `[['00ae4e40', '00ae4e6b']]`

## 命令位置別の参照

- [`00ae4dfc`](#insn-00ae4dfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae4e00`](#insn-00ae4e00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae4e10`](#insn-00ae4e10) → `010a0328`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae4e18`](#insn-00ae4e18) → [`00ae4e40`](#insn-00ae4e40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae4e20`](#insn-00ae4e20) → `002a7cd0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae4e34`](#insn-00ae4e34) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00ae4e3c`](#insn-00ae4e3c) → `010a0328`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae4e40`](#insn-00ae4e40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae4e50`](#insn-00ae4e50) → `002f5a58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae4e54`](#insn-00ae4e54) → `010a0348`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae4e58`](#insn-00ae4e58) → `002a7cd0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae4e68`](#insn-00ae4e68) → [`00bde020`](../00bde/00bde020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde020` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae4dfc`](#insn-00ae4dfc)

~~~json
{
  "source": "00ae4dfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae4e00`](#insn-00ae4e00)

~~~json
{
  "source": "00ae4e00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae4e10`](#insn-00ae4e10)

~~~json
{
  "source": "00ae4e10",
  "target": "010a0328",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0328",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae4e18`](#insn-00ae4e18)

~~~json
{
  "source": "00ae4e18",
  "target": "00ae4e40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae4e20`](#insn-00ae4e20)

~~~json
{
  "source": "00ae4e20",
  "target": "002a7cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7cd0",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f436c6173734c6f6164657200",
  "capture_start": "002a7cd0",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae4e34`](#insn-00ae4e34)

~~~json
{
  "source": "00ae4e34",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae4e3c`](#insn-00ae4e3c)

~~~json
{
  "source": "00ae4e3c",
  "target": "010a0328",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0328",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae4e40`](#insn-00ae4e40)

~~~json
{
  "source": "00ae4e40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae4e50`](#insn-00ae4e50)

~~~json
{
  "source": "00ae4e50",
  "target": "002f5a58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae4e54`](#insn-00ae4e54)

~~~json
{
  "source": "00ae4e54",
  "target": "010a0348",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae4e58`](#insn-00ae4e58)

~~~json
{
  "source": "00ae4e58",
  "target": "002a7cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7cd0",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f436c6173734c6f6164657200",
  "capture_start": "002a7cd0",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae4e68`](#insn-00ae4e68)

~~~json
{
  "source": "00ae4e68",
  "target": "00bde020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
