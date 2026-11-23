# 00aebfac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aec074`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec074.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-95b5419e3163d5195a84dc965051696f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebfac",
  "name": "_ZN8firebase4util4list12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "53ad75a8a3c8c20b330439316649414bc16d4e934a20cc9b4d0c2716e6669085",
  "source_text_sha256": "53ad75a8a3c8c20b330439316649414bc16d4e934a20cc9b4d0c2716e6669085",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebfac",
        "00aec04b"
      ]
    ],
    "bytes_sha256": "dbc3a5343b5f569f66da41fdeb1780af3d548cc50f89aca4401e8cca0a228905",
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

## 疑似コード / UTF-8 601 bytes

~~~c

void _ZN8firebase4util4list12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0820 != 0) {
    if (DAT_010a0828 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0828 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0820);
    DAT_010a0820 = 0;
  }
                    /* try { // try from 00aec03c to 00bec047 has its CatchHandler @ 00af1b68 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebfac"></a> `00aebfac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aebfb0"></a> `00aebfb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebfb4"></a> `00aebfb4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aebfb8"></a> `00aebfb8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aebfbc"></a> `00aebfbc` | `b4 2d 00 b0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebfc0"></a> `00aebfc0` | `81 12 44 f9` | ldr x1,[x20, #0x820] | `FALL_THROUGH`
<a id="insn-00aebfc4"></a> `00aebfc4` | `c1 03 00 b4` | cbz x1,0x00aec03c | `CONDITIONAL_JUMP`
<a id="insn-00aebfc8"></a> `00aebfc8` | `b5 2d 00 b0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebfcc"></a> `00aebfcc` | `a8 a2 60 39` | ldrb w8,[x21, #0x828] | `FALL_THROUGH`
<a id="insn-00aebfd0"></a> `00aebfd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aebfd4"></a> `00aebfd4` | `c8 00 00 34` | cbz w8,0x00aebfec | `CONDITIONAL_JUMP`
<a id="insn-00aebfd8"></a> `00aebfd8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aebfdc"></a> `00aebfdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebfe0"></a> `00aebfe0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aebfe4"></a> `00aebfe4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aebfe8"></a> `00aebfe8` | `bf a2 20 39` | strb wzr,[x21, #0x828] | `FALL_THROUGH`
<a id="insn-00aebfec"></a> `00aebfec` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aebff0"></a> `00aebff0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebff4"></a> `00aebff4` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aebff8"></a> `00aebff8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aebffc"></a> `00aebffc` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aec000"></a> `00aec000` | `20 01 00 54` | b.eq 0x00aec024 | `CONDITIONAL_JUMP`
<a id="insn-00aec004"></a> `00aec004` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aec008"></a> `00aec008` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec00c"></a> `00aec00c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aec010"></a> `00aec010` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec014"></a> `00aec014` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aec018"></a> `00aec018` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec01c"></a> `00aec01c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aec020"></a> `00aec020` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec024"></a> `00aec024` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aec028"></a> `00aec028` | `81 12 44 f9` | ldr x1,[x20, #0x820] | `FALL_THROUGH`
<a id="insn-00aec02c"></a> `00aec02c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec030"></a> `00aec030` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aec034"></a> `00aec034` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec038"></a> `00aec038` | `9f 12 04 f9` | str xzr,[x20, #0x820] | `FALL_THROUGH`
<a id="insn-00aec03c"></a> `00aec03c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aec040"></a> `00aec040` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec044"></a> `00aec044` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aec048"></a> `00aec048` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebfac`](#insn-00aebfac) 範囲 `[['00aebfac', '00aebfc7']]`
  - `CONDITIONAL_JUMP` [`00aebfc4`](#insn-00aebfc4) → [`00aec03c`](#insn-00aec03c)
  - `FALL_THROUGH` [`00aebfc4`](#insn-00aebfc4) → [`00aebfc8`](#insn-00aebfc8)
- ブロック [`00aebfc8`](#insn-00aebfc8) 範囲 `[['00aebfc8', '00aebfd7']]`
  - `CONDITIONAL_JUMP` [`00aebfd4`](#insn-00aebfd4) → [`00aebfec`](#insn-00aebfec)
  - `FALL_THROUGH` [`00aebfd4`](#insn-00aebfd4) → [`00aebfd8`](#insn-00aebfd8)
- ブロック [`00aebfd8`](#insn-00aebfd8) 範囲 `[['00aebfd8', '00aebfeb']]`
  - `FALL_THROUGH` [`00aebfe8`](#insn-00aebfe8) → [`00aebfec`](#insn-00aebfec)
- ブロック [`00aebfec`](#insn-00aebfec) 範囲 `[['00aebfec', '00aec003']]`
  - `CONDITIONAL_JUMP` [`00aec000`](#insn-00aec000) → [`00aec024`](#insn-00aec024)
  - `FALL_THROUGH` [`00aec000`](#insn-00aec000) → [`00aec004`](#insn-00aec004)
- ブロック [`00aec004`](#insn-00aec004) 範囲 `[['00aec004', '00aec023']]`
  - `FALL_THROUGH` [`00aec020`](#insn-00aec020) → [`00aec024`](#insn-00aec024)
- ブロック [`00aec024`](#insn-00aec024) 範囲 `[['00aec024', '00aec03b']]`
  - `FALL_THROUGH` [`00aec038`](#insn-00aec038) → [`00aec03c`](#insn-00aec03c)
- ブロック [`00aec03c`](#insn-00aec03c) 範囲 `[['00aec03c', '00aec04b']]`

## 命令位置別の参照

- [`00aebfac`](#insn-00aebfac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebfb0`](#insn-00aebfb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebfb4`](#insn-00aebfb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebfc0`](#insn-00aebfc0) → `010a0820`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebfc4`](#insn-00aebfc4) → [`00aec03c`](#insn-00aec03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebfcc`](#insn-00aebfcc) → `010a0828`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aebfd4`](#insn-00aebfd4) → [`00aebfec`](#insn-00aebfec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebfe8`](#insn-00aebfe8) → `010a0828`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aec000`](#insn-00aec000) → [`00aec024`](#insn-00aec024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec028`](#insn-00aec028) → `010a0820`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec038`](#insn-00aec038) → `010a0820`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec03c`](#insn-00aec03c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec040`](#insn-00aec040) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebfac`](#insn-00aebfac)

~~~json
{
  "source": "00aebfac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebfb0`](#insn-00aebfb0)

~~~json
{
  "source": "00aebfb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebfb4`](#insn-00aebfb4)

~~~json
{
  "source": "00aebfb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebfc0`](#insn-00aebfc0)

~~~json
{
  "source": "00aebfc0",
  "target": "010a0820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0820",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebfc4`](#insn-00aebfc4)

~~~json
{
  "source": "00aebfc4",
  "target": "00aec03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebfcc`](#insn-00aebfcc)

~~~json
{
  "source": "00aebfcc",
  "target": "010a0828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0828",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebfd4`](#insn-00aebfd4)

~~~json
{
  "source": "00aebfd4",
  "target": "00aebfec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebfe8`](#insn-00aebfe8)

~~~json
{
  "source": "00aebfe8",
  "target": "010a0828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0828",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec000`](#insn-00aec000)

~~~json
{
  "source": "00aec000",
  "target": "00aec024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec028`](#insn-00aec028)

~~~json
{
  "source": "00aec028",
  "target": "010a0820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0820",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec038`](#insn-00aec038)

~~~json
{
  "source": "00aec038",
  "target": "010a0820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0820",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec03c`](#insn-00aec03c)

~~~json
{
  "source": "00aec03c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec040`](#insn-00aec040)

~~~json
{
  "source": "00aec040",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
