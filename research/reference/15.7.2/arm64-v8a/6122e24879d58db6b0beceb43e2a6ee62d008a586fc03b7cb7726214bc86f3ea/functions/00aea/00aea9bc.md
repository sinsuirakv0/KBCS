# 00aea9bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeaa84`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaa84.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-0b10f72874a3b9907a4518ec641e3792)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aea9bc",
  "name": "_ZN8firebase4util11float_class12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "27bfc38a9cf324673dce9334da7470ab852ed12382d03542e733ce2c9249a8e3",
  "source_text_sha256": "27bfc38a9cf324673dce9334da7470ab852ed12382d03542e733ce2c9249a8e3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aea9bc",
        "00aeaa5b"
      ]
    ],
    "bytes_sha256": "cc45a277ff8e2766b79d86198539e0fff50bbfbd1df8c8449997c2d4ef2823ac",
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

## 疑似コード / UTF-8 599 bytes

~~~c

void _ZN8firebase4util11float_class12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0728 != 0) {
    if (DAT_010a0730 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0730 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
                    /* catch() { ... } // from try @ 00aeac14 with catch @ 00aeaa38 */
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0728);
    DAT_010a0728 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aea9bc"></a> `00aea9bc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aea9c0"></a> `00aea9c0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea9c4"></a> `00aea9c4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aea9c8"></a> `00aea9c8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aea9cc"></a> `00aea9cc` | `b4 2d 00 d0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aea9d0"></a> `00aea9d0` | `81 96 43 f9` | ldr x1,[x20, #0x728] | `FALL_THROUGH`
<a id="insn-00aea9d4"></a> `00aea9d4` | `c1 03 00 b4` | cbz x1,0x00aeaa4c | `CONDITIONAL_JUMP`
<a id="insn-00aea9d8"></a> `00aea9d8` | `b5 2d 00 d0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aea9dc"></a> `00aea9dc` | `a8 c2 5c 39` | ldrb w8,[x21, #0x730] | `FALL_THROUGH`
<a id="insn-00aea9e0"></a> `00aea9e0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aea9e4"></a> `00aea9e4` | `c8 00 00 34` | cbz w8,0x00aea9fc | `CONDITIONAL_JUMP`
<a id="insn-00aea9e8"></a> `00aea9e8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aea9ec"></a> `00aea9ec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea9f0"></a> `00aea9f0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aea9f4"></a> `00aea9f4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aea9f8"></a> `00aea9f8` | `bf c2 1c 39` | strb wzr,[x21, #0x730] | `FALL_THROUGH`
<a id="insn-00aea9fc"></a> `00aea9fc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeaa00"></a> `00aeaa00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaa04"></a> `00aeaa04` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aeaa08"></a> `00aeaa08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeaa0c"></a> `00aeaa0c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aeaa10"></a> `00aeaa10` | `20 01 00 54` | b.eq 0x00aeaa34 | `CONDITIONAL_JUMP`
<a id="insn-00aeaa14"></a> `00aeaa14` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeaa18"></a> `00aeaa18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaa1c"></a> `00aeaa1c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aeaa20"></a> `00aeaa20` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeaa24"></a> `00aeaa24` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeaa28"></a> `00aeaa28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaa2c"></a> `00aeaa2c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aeaa30"></a> `00aeaa30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeaa34"></a> `00aeaa34` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeaa38"></a> `00aeaa38` | `81 96 43 f9` | ldr x1,[x20, #0x728] | `FALL_THROUGH`
<a id="insn-00aeaa3c"></a> `00aeaa3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaa40"></a> `00aeaa40` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aeaa44"></a> `00aeaa44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeaa48"></a> `00aeaa48` | `9f 96 03 f9` | str xzr,[x20, #0x728] | `FALL_THROUGH`
<a id="insn-00aeaa4c"></a> `00aeaa4c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeaa50"></a> `00aeaa50` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaa54"></a> `00aeaa54` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aeaa58"></a> `00aeaa58` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aea9bc`](#insn-00aea9bc) 範囲 `[['00aea9bc', '00aea9d7']]`
  - `CONDITIONAL_JUMP` [`00aea9d4`](#insn-00aea9d4) → [`00aeaa4c`](#insn-00aeaa4c)
  - `FALL_THROUGH` [`00aea9d4`](#insn-00aea9d4) → [`00aea9d8`](#insn-00aea9d8)
- ブロック [`00aea9d8`](#insn-00aea9d8) 範囲 `[['00aea9d8', '00aea9e7']]`
  - `CONDITIONAL_JUMP` [`00aea9e4`](#insn-00aea9e4) → [`00aea9fc`](#insn-00aea9fc)
  - `FALL_THROUGH` [`00aea9e4`](#insn-00aea9e4) → [`00aea9e8`](#insn-00aea9e8)
- ブロック [`00aea9e8`](#insn-00aea9e8) 範囲 `[['00aea9e8', '00aea9fb']]`
  - `FALL_THROUGH` [`00aea9f8`](#insn-00aea9f8) → [`00aea9fc`](#insn-00aea9fc)
- ブロック [`00aea9fc`](#insn-00aea9fc) 範囲 `[['00aea9fc', '00aeaa13']]`
  - `CONDITIONAL_JUMP` [`00aeaa10`](#insn-00aeaa10) → [`00aeaa34`](#insn-00aeaa34)
  - `FALL_THROUGH` [`00aeaa10`](#insn-00aeaa10) → [`00aeaa14`](#insn-00aeaa14)
- ブロック [`00aeaa14`](#insn-00aeaa14) 範囲 `[['00aeaa14', '00aeaa33']]`
  - `FALL_THROUGH` [`00aeaa30`](#insn-00aeaa30) → [`00aeaa34`](#insn-00aeaa34)
- ブロック [`00aeaa34`](#insn-00aeaa34) 範囲 `[['00aeaa34', '00aeaa37']]`
  - `FALL_THROUGH` [`00aeaa34`](#insn-00aeaa34) → [`00aeaa38`](#insn-00aeaa38)
- ブロック [`00aeaa38`](#insn-00aeaa38) 範囲 `[['00aeaa38', '00aeaa4b']]`
  - `FALL_THROUGH` [`00aeaa48`](#insn-00aeaa48) → [`00aeaa4c`](#insn-00aeaa4c)
- ブロック [`00aeaa4c`](#insn-00aeaa4c) 範囲 `[['00aeaa4c', '00aeaa5b']]`

## 命令位置別の参照

- [`00aea9bc`](#insn-00aea9bc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea9c0`](#insn-00aea9c0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea9c4`](#insn-00aea9c4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea9d0`](#insn-00aea9d0) → `010a0728`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aea9d4`](#insn-00aea9d4) → [`00aeaa4c`](#insn-00aeaa4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea9dc`](#insn-00aea9dc) → `010a0730`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aea9e4`](#insn-00aea9e4) → [`00aea9fc`](#insn-00aea9fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea9f8`](#insn-00aea9f8) → `010a0730`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeaa10`](#insn-00aeaa10) → [`00aeaa34`](#insn-00aeaa34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaa38`](#insn-00aeaa38) → `010a0728`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaa48`](#insn-00aeaa48) → `010a0728`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaa4c`](#insn-00aeaa4c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaa50`](#insn-00aeaa50) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aea9bc`](#insn-00aea9bc)

~~~json
{
  "source": "00aea9bc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea9c0`](#insn-00aea9c0)

~~~json
{
  "source": "00aea9c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea9c4`](#insn-00aea9c4)

~~~json
{
  "source": "00aea9c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea9d0`](#insn-00aea9d0)

~~~json
{
  "source": "00aea9d0",
  "target": "010a0728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0728",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea9d4`](#insn-00aea9d4)

~~~json
{
  "source": "00aea9d4",
  "target": "00aeaa4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea9dc`](#insn-00aea9dc)

~~~json
{
  "source": "00aea9dc",
  "target": "010a0730",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0730",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea9e4`](#insn-00aea9e4)

~~~json
{
  "source": "00aea9e4",
  "target": "00aea9fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea9f8`](#insn-00aea9f8)

~~~json
{
  "source": "00aea9f8",
  "target": "010a0730",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0730",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaa10`](#insn-00aeaa10)

~~~json
{
  "source": "00aeaa10",
  "target": "00aeaa34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaa38`](#insn-00aeaa38)

~~~json
{
  "source": "00aeaa38",
  "target": "010a0728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0728",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaa48`](#insn-00aeaa48)

~~~json
{
  "source": "00aeaa48",
  "target": "010a0728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0728",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaa4c`](#insn-00aeaa4c)

~~~json
{
  "source": "00aeaa4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaa50`](#insn-00aeaa50)

~~~json
{
  "source": "00aeaa50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
