module tb_encoder;

    reg d0, d1, d2, d3;
    wire y1, y0;

    encoder_4to2 uut (
        .D0(d0),
        .D1(d1),
        .D2(d2),
        .D3(d3),
        .Y1(y1),
        .Y0(y0)
    );

    initial begin
        $dumpfile("encoder.vcd");
        $dumpvars(0, tb_encoder);

        $display("D3 D2 D1 D0 | Y1 Y0");
        $display("---------------------");

        d3=0; d2=0; d1=0; d0=1; #10;
        $display("%b  %b  %b  %b  | %b  %b", d3,d2,d1,d0,y1,y0);

        d3=0; d2=0; d1=1; d0=0; #10;
        $display("%b  %b  %b  %b  | %b  %b", d3,d2,d1,d0,y1,y0);

        d3=0; d2=1; d1=0; d0=0; #10;
        $display("%b  %b  %b  %b  | %b  %b", d3,d2,d1,d0,y1,y0);

        d3=1; d2=0; d1=0; d0=0; #10;
        $display("%b  %b  %b  %b  | %b  %b", d3,d2,d1,d0,y1,y0);

        $finish;
    end

endmodule
