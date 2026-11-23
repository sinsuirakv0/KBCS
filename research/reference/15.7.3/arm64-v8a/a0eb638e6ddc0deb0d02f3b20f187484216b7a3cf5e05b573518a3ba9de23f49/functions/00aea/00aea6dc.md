# 00aea6dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aea614`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea614.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-eebd3c82e76a3d118ab4e51be87fe476)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aea720`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea720.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0063.md#compare-c3ff6caafff791b3f437f642a47dc486)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aea6dc",
  "name": "_ZN8firebase4util4file12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "365f38332152cd23727d7c1123d10e5a39c6cd893d5fee7d25225f1f6c5608a5",
  "source_text_sha256": "365f38332152cd23727d7c1123d10e5a39c6cd893d5fee7d25225f1f6c5608a5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aea6dc",
        "00aea77b"
      ]
    ],
    "bytes_sha256": "6d884eb78e79bd4e10c1a762aae6739f64edd71c8fa62fdb55e3c0cbe8eb4f71",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 504 bytes

~~~c

void _ZN8firebase4util4file12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0790 != 0) {
    if (DAT_010a0798 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0798 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0790);
    DAT_010a0790 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aea6dc"></a> `00aea6dc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aea6e0"></a> `00aea6e0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea6e4"></a> `00aea6e4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aea6e8"></a> `00aea6e8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aea6ec"></a> `00aea6ec` | `b4 2d 00 d0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aea6f0"></a> `00aea6f0` | `81 ca 43 f9` | ldr x1,[x20, #0x790] | `FALL_THROUGH`
<a id="insn-00aea6f4"></a> `00aea6f4` | `c1 03 00 b4` | cbz x1,0x00aea76c | `CONDITIONAL_JUMP`
<a id="insn-00aea6f8"></a> `00aea6f8` | `b5 2d 00 d0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aea6fc"></a> `00aea6fc` | `a8 62 5e 39` | ldrb w8,[x21, #0x798] | `FALL_THROUGH`
<a id="insn-00aea700"></a> `00aea700` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aea704"></a> `00aea704` | `c8 00 00 34` | cbz w8,0x00aea71c | `CONDITIONAL_JUMP`
<a id="insn-00aea708"></a> `00aea708` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aea70c"></a> `00aea70c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea710"></a> `00aea710` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aea714"></a> `00aea714` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aea718"></a> `00aea718` | `bf 62 1e 39` | strb wzr,[x21, #0x798] | `FALL_THROUGH`
<a id="insn-00aea71c"></a> `00aea71c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aea720"></a> `00aea720` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea724"></a> `00aea724` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aea728"></a> `00aea728` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aea72c"></a> `00aea72c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aea730"></a> `00aea730` | `20 01 00 54` | b.eq 0x00aea754 | `CONDITIONAL_JUMP`
<a id="insn-00aea734"></a> `00aea734` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aea738"></a> `00aea738` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea73c"></a> `00aea73c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aea740"></a> `00aea740` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aea744"></a> `00aea744` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aea748"></a> `00aea748` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea74c"></a> `00aea74c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aea750"></a> `00aea750` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aea754"></a> `00aea754` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aea758"></a> `00aea758` | `81 ca 43 f9` | ldr x1,[x20, #0x790] | `FALL_THROUGH`
<a id="insn-00aea75c"></a> `00aea75c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea760"></a> `00aea760` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aea764"></a> `00aea764` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aea768"></a> `00aea768` | `9f ca 03 f9` | str xzr,[x20, #0x790] | `FALL_THROUGH`
<a id="insn-00aea76c"></a> `00aea76c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aea770"></a> `00aea770` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea774"></a> `00aea774` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aea778"></a> `00aea778` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aea6dc`](#insn-00aea6dc) 範囲 `[['00aea6dc', '00aea6f7']]`
  - `CONDITIONAL_JUMP` [`00aea6f4`](#insn-00aea6f4) → [`00aea76c`](#insn-00aea76c)
  - `FALL_THROUGH` [`00aea6f4`](#insn-00aea6f4) → [`00aea6f8`](#insn-00aea6f8)
- ブロック [`00aea6f8`](#insn-00aea6f8) 範囲 `[['00aea6f8', '00aea707']]`
  - `CONDITIONAL_JUMP` [`00aea704`](#insn-00aea704) → [`00aea71c`](#insn-00aea71c)
  - `FALL_THROUGH` [`00aea704`](#insn-00aea704) → [`00aea708`](#insn-00aea708)
- ブロック [`00aea708`](#insn-00aea708) 範囲 `[['00aea708', '00aea71b']]`
  - `FALL_THROUGH` [`00aea718`](#insn-00aea718) → [`00aea71c`](#insn-00aea71c)
- ブロック [`00aea71c`](#insn-00aea71c) 範囲 `[['00aea71c', '00aea733']]`
  - `CONDITIONAL_JUMP` [`00aea730`](#insn-00aea730) → [`00aea754`](#insn-00aea754)
  - `FALL_THROUGH` [`00aea730`](#insn-00aea730) → [`00aea734`](#insn-00aea734)
- ブロック [`00aea734`](#insn-00aea734) 範囲 `[['00aea734', '00aea753']]`
  - `FALL_THROUGH` [`00aea750`](#insn-00aea750) → [`00aea754`](#insn-00aea754)
- ブロック [`00aea754`](#insn-00aea754) 範囲 `[['00aea754', '00aea76b']]`
  - `FALL_THROUGH` [`00aea768`](#insn-00aea768) → [`00aea76c`](#insn-00aea76c)
- ブロック [`00aea76c`](#insn-00aea76c) 範囲 `[['00aea76c', '00aea77b']]`

## 命令位置別の参照

- [`00aea6dc`](#insn-00aea6dc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea6e0`](#insn-00aea6e0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea6e4`](#insn-00aea6e4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea6f0`](#insn-00aea6f0) → `010a0790`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aea6f4`](#insn-00aea6f4) → [`00aea76c`](#insn-00aea76c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea6fc`](#insn-00aea6fc) → `010a0798`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aea704`](#insn-00aea704) → [`00aea71c`](#insn-00aea71c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea718`](#insn-00aea718) → `010a0798`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aea730`](#insn-00aea730) → [`00aea754`](#insn-00aea754) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea758`](#insn-00aea758) → `010a0790`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aea768`](#insn-00aea768) → `010a0790`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aea76c`](#insn-00aea76c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea770`](#insn-00aea770) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aea6dc`](#insn-00aea6dc)

~~~json
{
  "source": "00aea6dc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea6e0`](#insn-00aea6e0)

~~~json
{
  "source": "00aea6e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea6e4`](#insn-00aea6e4)

~~~json
{
  "source": "00aea6e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea6f0`](#insn-00aea6f0)

~~~json
{
  "source": "00aea6f0",
  "target": "010a0790",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0790",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea6f4`](#insn-00aea6f4)

~~~json
{
  "source": "00aea6f4",
  "target": "00aea76c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea6fc`](#insn-00aea6fc)

~~~json
{
  "source": "00aea6fc",
  "target": "010a0798",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0798",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea704`](#insn-00aea704)

~~~json
{
  "source": "00aea704",
  "target": "00aea71c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea718`](#insn-00aea718)

~~~json
{
  "source": "00aea718",
  "target": "010a0798",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0798",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea730`](#insn-00aea730)

~~~json
{
  "source": "00aea730",
  "target": "00aea754",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea758`](#insn-00aea758)

~~~json
{
  "source": "00aea758",
  "target": "010a0790",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0790",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea768`](#insn-00aea768)

~~~json
{
  "source": "00aea768",
  "target": "010a0790",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0790",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea76c`](#insn-00aea76c)

~~~json
{
  "source": "00aea76c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea770`](#insn-00aea770)

~~~json
{
  "source": "00aea770",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
