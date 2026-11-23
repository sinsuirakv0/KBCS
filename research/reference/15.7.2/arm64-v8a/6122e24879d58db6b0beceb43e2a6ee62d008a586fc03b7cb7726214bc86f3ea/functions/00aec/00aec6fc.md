# 00aec6fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aec7c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec7c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-96ec0f4cd07483063968823ff19b07da)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aec6fc",
  "name": "_ZN8firebase4util3map12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb3f6321f0a4505243facb2544bb804d178d9072cdb1c4ee8bd9cc3f9385fe25",
  "source_text_sha256": "eb3f6321f0a4505243facb2544bb804d178d9072cdb1c4ee8bd9cc3f9385fe25",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aec6fc",
        "00aec79b"
      ]
    ],
    "bytes_sha256": "97a66b3e945f1f74d546221be19329f6d0b418fdb20cacec75e664b91d500b71",
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

## 疑似コード / UTF-8 503 bytes

~~~c

void _ZN8firebase4util3map12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0878 != 0) {
    if (DAT_010a0880 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0880 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0878);
    DAT_010a0878 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aec6fc"></a> `00aec6fc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aec700"></a> `00aec700` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec704"></a> `00aec704` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aec708"></a> `00aec708` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aec70c"></a> `00aec70c` | `b4 2d 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aec710"></a> `00aec710` | `81 3e 44 f9` | ldr x1,[x20, #0x878] | `FALL_THROUGH`
<a id="insn-00aec714"></a> `00aec714` | `c1 03 00 b4` | cbz x1,0x00aec78c | `CONDITIONAL_JUMP`
<a id="insn-00aec718"></a> `00aec718` | `b5 2d 00 90` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aec71c"></a> `00aec71c` | `a8 02 62 39` | ldrb w8,[x21, #0x880] | `FALL_THROUGH`
<a id="insn-00aec720"></a> `00aec720` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aec724"></a> `00aec724` | `c8 00 00 34` | cbz w8,0x00aec73c | `CONDITIONAL_JUMP`
<a id="insn-00aec728"></a> `00aec728` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aec72c"></a> `00aec72c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec730"></a> `00aec730` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aec734"></a> `00aec734` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec738"></a> `00aec738` | `bf 02 22 39` | strb wzr,[x21, #0x880] | `FALL_THROUGH`
<a id="insn-00aec73c"></a> `00aec73c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aec740"></a> `00aec740` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec744"></a> `00aec744` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aec748"></a> `00aec748` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec74c"></a> `00aec74c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aec750"></a> `00aec750` | `20 01 00 54` | b.eq 0x00aec774 | `CONDITIONAL_JUMP`
<a id="insn-00aec754"></a> `00aec754` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aec758"></a> `00aec758` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec75c"></a> `00aec75c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aec760"></a> `00aec760` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec764"></a> `00aec764` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aec768"></a> `00aec768` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec76c"></a> `00aec76c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aec770"></a> `00aec770` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec774"></a> `00aec774` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aec778"></a> `00aec778` | `81 3e 44 f9` | ldr x1,[x20, #0x878] | `FALL_THROUGH`
<a id="insn-00aec77c"></a> `00aec77c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec780"></a> `00aec780` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aec784"></a> `00aec784` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec788"></a> `00aec788` | `9f 3e 04 f9` | str xzr,[x20, #0x878] | `FALL_THROUGH`
<a id="insn-00aec78c"></a> `00aec78c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aec790"></a> `00aec790` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec794"></a> `00aec794` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aec798"></a> `00aec798` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aec6fc`](#insn-00aec6fc) 範囲 `[['00aec6fc', '00aec717']]`
  - `CONDITIONAL_JUMP` [`00aec714`](#insn-00aec714) → [`00aec78c`](#insn-00aec78c)
  - `FALL_THROUGH` [`00aec714`](#insn-00aec714) → [`00aec718`](#insn-00aec718)
- ブロック [`00aec718`](#insn-00aec718) 範囲 `[['00aec718', '00aec727']]`
  - `CONDITIONAL_JUMP` [`00aec724`](#insn-00aec724) → [`00aec73c`](#insn-00aec73c)
  - `FALL_THROUGH` [`00aec724`](#insn-00aec724) → [`00aec728`](#insn-00aec728)
- ブロック [`00aec728`](#insn-00aec728) 範囲 `[['00aec728', '00aec73b']]`
  - `FALL_THROUGH` [`00aec738`](#insn-00aec738) → [`00aec73c`](#insn-00aec73c)
- ブロック [`00aec73c`](#insn-00aec73c) 範囲 `[['00aec73c', '00aec753']]`
  - `CONDITIONAL_JUMP` [`00aec750`](#insn-00aec750) → [`00aec774`](#insn-00aec774)
  - `FALL_THROUGH` [`00aec750`](#insn-00aec750) → [`00aec754`](#insn-00aec754)
- ブロック [`00aec754`](#insn-00aec754) 範囲 `[['00aec754', '00aec773']]`
  - `FALL_THROUGH` [`00aec770`](#insn-00aec770) → [`00aec774`](#insn-00aec774)
- ブロック [`00aec774`](#insn-00aec774) 範囲 `[['00aec774', '00aec78b']]`
  - `FALL_THROUGH` [`00aec788`](#insn-00aec788) → [`00aec78c`](#insn-00aec78c)
- ブロック [`00aec78c`](#insn-00aec78c) 範囲 `[['00aec78c', '00aec79b']]`

## 命令位置別の参照

- [`00aec6fc`](#insn-00aec6fc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec700`](#insn-00aec700) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec704`](#insn-00aec704) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec710`](#insn-00aec710) → `010a0878`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec714`](#insn-00aec714) → [`00aec78c`](#insn-00aec78c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec71c`](#insn-00aec71c) → `010a0880`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aec724`](#insn-00aec724) → [`00aec73c`](#insn-00aec73c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec738`](#insn-00aec738) → `010a0880`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aec750`](#insn-00aec750) → [`00aec774`](#insn-00aec774) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec778`](#insn-00aec778) → `010a0878`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec788`](#insn-00aec788) → `010a0878`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec78c`](#insn-00aec78c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec790`](#insn-00aec790) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aec6fc`](#insn-00aec6fc)

~~~json
{
  "source": "00aec6fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec700`](#insn-00aec700)

~~~json
{
  "source": "00aec700",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec704`](#insn-00aec704)

~~~json
{
  "source": "00aec704",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec710`](#insn-00aec710)

~~~json
{
  "source": "00aec710",
  "target": "010a0878",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0878",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec714`](#insn-00aec714)

~~~json
{
  "source": "00aec714",
  "target": "00aec78c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec71c`](#insn-00aec71c)

~~~json
{
  "source": "00aec71c",
  "target": "010a0880",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0880",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec724`](#insn-00aec724)

~~~json
{
  "source": "00aec724",
  "target": "00aec73c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec738`](#insn-00aec738)

~~~json
{
  "source": "00aec738",
  "target": "010a0880",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0880",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec750`](#insn-00aec750)

~~~json
{
  "source": "00aec750",
  "target": "00aec774",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec778`](#insn-00aec778)

~~~json
{
  "source": "00aec778",
  "target": "010a0878",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0878",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec788`](#insn-00aec788)

~~~json
{
  "source": "00aec788",
  "target": "010a0878",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0878",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec78c`](#insn-00aec78c)

~~~json
{
  "source": "00aec78c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec790`](#insn-00aec790)

~~~json
{
  "source": "00aec790",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
